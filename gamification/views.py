from django.core.paginator import Paginator
from django.shortcuts import render
from django.utils import timezone
from django_rq import get_queue

from .models import FosUserUser, GamificationChallenge
from .handler import process_relevant_challenges


def fos_user_user(request):
    user_list = FosUserUser.objects.order_by( 'id' )
    paginator = Paginator( user_list, 30 )
    page_number = request.GET.get( 'page' )
    page_obj = paginator.get_page( page_number )
    return render( request, 'fos_user_user.html', {'fos_user_users': page_obj} )


def gamification_challenge_view(request):
    challenges_list = GamificationChallenge.objects.all().order_by( 'id' )
    paginator = Paginator( challenges_list, 20 )
    page_number = request.GET.get( 'page' )
    page_obj = paginator.get_page( page_number )
    return render( request, 'gamification_challenge.html', {'paginated_challenges': page_obj} )


def process_and_update_mongo(request):
    gamif_challenges = GamificationChallenge.objects.filter( end_date__gt=timezone.now() )
    challenge_ids = list( gamif_challenges.values_list( 'id', flat=True ) )

    num_queues = 5  # Total number of queues
    queue_names = [f'gamification_challenges{i + 1}' for i in range( num_queues )]

    for index, challenge_id in enumerate( challenge_ids ):
        queue_name = queue_names[index % num_queues]
        queue = get_queue( queue_name )
        # Enqueue each challenge ID independently
        queue.enqueue( process_relevant_challenges, [challenge_id])

    return render( request, 'challenge_queue.html' )
