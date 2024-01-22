from django.db import models
from django.utils import timezone


class AppVersion(models.Model):
    id = models.AutoField(primary_key=True)
    is_deleted = models.BooleanField(null=True)
    modifiedby = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    version = models.CharField(max_length=255)
    status = models.BooleanField()
    current_release = models.BooleanField()
    fos_user_user = models.ManyToManyField('FosUserUser', related_name='app_versions')

    class Meta:
        db_table = 'app_version'


class UserEmergency(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(null=True)
    is_deleted = models.BooleanField(null=True)
    modifiedby = models.IntegerField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    firstName = models.CharField(max_length=255, null=True)
    lastName = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    phoneNumber = models.CharField(max_length=255, null=True)
    fos_user_user = models.ForeignKey('FosUserUser', on_delete=models.RESTRICT, null=True,
                                      related_name='user_emergencies')

    class Meta:
        db_table = 'UserEmergency'


class UserHealthAnalytic(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_sleep_well = models.BooleanField(null=True)
    water_intake = models.IntegerField(null=True)
    breath_count = models.IntegerField(null=True)
    step_count = models.IntegerField(null=True)
    heart_rate = models.IntegerField(null=True)
    watched_content = models.IntegerField(null=True)
    calories_count = models.FloatField(null=True)
    stat_type = models.CharField(max_length=255, null=True)
    user = models.ForeignKey('FosUserUser', on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_health_analytic'


class BookingWhiteLabelUser(models.Model):
    id = models.AutoField(primary_key=True)
    bookingwhitelabel_id = models.IntegerField()
    user_id = models.IntegerField()
    fos_user_user = models.ForeignKey('FosUserUser', on_delete=models.CASCADE, related_name='bookingwhitelabel_users')

    class Meta:
        db_table = 'bookingwhitelabel_user'


class Challenge(models.Model):
    id = models.AutoField(primary_key=True)
    company_id = models.IntegerField(null=True)
    is_deleted = models.BooleanField(null=True)
    modifiedby = models.IntegerField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    title = models.CharField(max_length=255)
    logo_name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField()
    code = models.CharField(max_length=255, unique=True, db_index=True)
    fos_user_user = models.ForeignKey('FosUserUser', on_delete=models.RESTRICT, null=True, related_name='challenges')

    class Meta:
        db_table = 'challenge'


class CorporateDepartment(models.Model):
    id = models.AutoField(primary_key=True)
    corporate_id = models.IntegerField(null=True)
    is_deleted = models.BooleanField(null=True)
    modifiedby = models.IntegerField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    code = models.CharField(max_length=25)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    imageName = models.CharField(max_length=255, null=True)
    fos_user_user = models.ForeignKey('FosUserUser', on_delete=models.RESTRICT, null=True,
                                      related_name='corporate_departments')

    class Meta:
        db_table = 'corporate_department'


class CorporateKey(models.Model):
    id = models.AutoField(primary_key=True)
    is_deleted = models.BooleanField(null=True)
    modifiedby = models.IntegerField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    company_key = models.CharField(max_length=25)
    validate_date = models.DateTimeField()
    start_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    fos_user_user = models.ForeignKey('FosUserUser', on_delete=models.RESTRICT, null=True,
                                      related_name='corporate_keys')

    class Meta:
        db_table = 'corporate_key'


class DeviceConfig(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(null=True)
    config = models.TextField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    fos_user_user = models.ForeignKey('FosUserUser', on_delete=models.CASCADE, null=True, related_name='device_configs')

    class Meta:
        db_table = 'device_config'


class Exercise(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(null=True)
    is_deleted = models.BooleanField(null=True)
    modifiedby = models.IntegerField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    image_name = models.CharField(max_length=255, null=True)
    video_name = models.CharField(max_length=255, null=True)
    point = models.IntegerField(null=True)
    time = models.IntegerField(null=True)
    description_ar = models.TextField(null=True)
    name_ar = models.TextField(null=True)
    fos_user_user = models.ForeignKey('FosUserUser', on_delete=models.RESTRICT, null=True, related_name='exercises')

    class Meta:
        db_table = 'exercise'


class FacilityActivity(models.Model):
    id = models.AutoField(primary_key=True)
    facility_id = models.IntegerField(null=True)
    activity_id = models.IntegerField(null=True)
    is_deleted = models.BooleanField(null=True)
    modifiedby = models.IntegerField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    is_recommended = models.BooleanField(default=False)
    fos_user_user = models.ForeignKey('FosUserUser', on_delete=models.RESTRICT, null=True,
                                      related_name='facility_activities')

    class Meta:
        db_table = 'facility_activity'


class FacilityAmenity(models.Model):
    id = models.AutoField(primary_key=True)
    facility_id = models.IntegerField(null=True)
    amenity_id = models.IntegerField(null=True)
    is_deleted = models.BooleanField(null=True)
    modifiedby = models.IntegerField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    fos_user_user = models.ForeignKey('FosUserUser', on_delete=models.RESTRICT, null=True,
                                      related_name='facility_amenities')

    class Meta:
        db_table = 'facility_amenitiy'


class FacilityCheckinHistory(models.Model):
    id = models.AutoField(primary_key=True)
    facility_id = models.IntegerField(null=True)
    member_id = models.IntegerField(null=True)
    is_deleted = models.BooleanField(null=True)
    modifiedby = models.IntegerField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    checkin = models.IntegerField(default=0)
    time = models.DateTimeField()
    fos_user_user_facility_checkin_history_facility_id = models.ForeignKey('FosUserUser', on_delete=models.RESTRICT,
                                                                           null=True,
                                                                           related_name='facility_checkin_history_facility_id')
    fos_user_user_facility_checkin_history_member_id = models.ForeignKey('FosUserUser', on_delete=models.RESTRICT,
                                                                         null=True,
                                                                         related_name='facility_checkin_history_member_id')

    class Meta:
        db_table = 'facility_checkin_history'


class FacilityGallery(models.Model):
    id = models.AutoField(primary_key=True)
    facility_id = models.IntegerField(null=True)
    is_deleted = models.BooleanField(null=True)
    modifiedby = models.IntegerField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    image_name = models.CharField(max_length=255, null=True)
    sequence = models.IntegerField(null=True)
    fos_user_user = models.ForeignKey('FosUserUser', on_delete=models.RESTRICT, null=True,
                                      related_name='facility_galleries')

    class Meta:
        db_table = 'facility_gallery'


class FacilityPackage(models.Model):
    id = models.AutoField(primary_key=True)
    facility_id = models.IntegerField(null=True)
    package_id = models.IntegerField(null=True)
    is_deleted = models.BooleanField(null=True)
    modifiedby = models.IntegerField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    fos_user_user = models.ForeignKey('FosUserUser', related_name='facility_packages', on_delete=models.CASCADE)

    class Meta:
        db_table = 'facility_package'


class FosUserUserGroup(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    group_id = models.IntegerField()
    fos_user_user = models.ForeignKey('FosUserUser', on_delete=models.CASCADE, related_name='user_groups')

    class Meta:
        db_table = 'fos_user_group'


class Instructor(models.Model):
    id = models.AutoField(primary_key=True)
    provider_id = models.IntegerField(null=True)
    is_deleted = models.BooleanField(default=False)
    modifiedby = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255, null=True)
    image = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.CharField(max_length=180, null=True)
    phone = models.CharField(max_length=64, null=True)
    emergency_phone = models.CharField(max_length=64, null=True)
    fos_user_user = models.ForeignKey('FosUserUser', on_delete=models.RESTRICT, null=True, related_name='instructors')

    class Meta:
        db_table = 'instructor'


class ManualCheckinHistory(models.Model):
    id = models.AutoField(primary_key=True)
    activity_id = models.IntegerField(null=True)
    member_id = models.IntegerField(null=True)
    is_deleted = models.BooleanField(default=False)
    modifiedby = models.IntegerField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    time = models.DateTimeField()
    fos_user_user = models.ForeignKey('FosUserUser', on_delete=models.RESTRICT, related_name='manual_checkins')

    class Meta:
        db_table = 'manual_checkin_history'


class MemberAction(models.Model):
    id = models.AutoField(primary_key=True)
    member_id = models.IntegerField(null=True)
    action_id = models.IntegerField(null=True)
    is_deleted = models.BooleanField(default=False)
    modifiedby = models.IntegerField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    isCompleted = models.BooleanField(null=True)
    value = models.CharField(max_length=255, null=True)
    fos_user_user = models.ForeignKey('FosUserUser', on_delete=models.RESTRICT, related_name='member_actions')

    class Meta:
        db_table = 'member_action'


class MemberActionPoint(models.Model):
    id = models.AutoField(primary_key=True)
    member_id = models.IntegerField(null=True)
    action_id = models.IntegerField(null=True)
    is_deleted = models.BooleanField(default=False)
    modifiedby = models.IntegerField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    action_date = models.DateField()
    fos_user_user = models.ForeignKey('FosUserUser', on_delete=models.RESTRICT, related_name='member_action_points')

    class Meta:
        db_table = 'member_action_point'


class MemberArticle(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    article_id = models.IntegerField()
    key_id = models.IntegerField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    fos_user_user = models.ForeignKey('FosUserUser', on_delete=models.CASCADE, related_name='member_articles')

    class Meta:
        db_table = 'member_article'


class MemberBilling(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    charge_id = models.CharField(max_length=100)
    track_id = models.CharField(max_length=100)
    card_id = models.CharField(max_length=100)
    last_four = models.CharField(max_length=4)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    vat = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    transaction_response = models.TextField()
    transaction_type = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    payment_gateway_used = models.CharField(max_length=50)
    failure_code = models.CharField(max_length=255, null=True)
    product_purchased = models.CharField(max_length=255, null=True)
    fos_user_user = models.ForeignKey('FosUserUser', on_delete=models.RESTRICT, related_name='member_billing')

    class Meta:
        db_table = 'member_billing'


class MemberChallengeInvite(models.Model):
    id = models.AutoField(primary_key=True)
    member_id = models.IntegerField(null=True)
    challenge_id = models.IntegerField(null=True)
    is_deleted = models.BooleanField(default=False)
    modifiedby = models.IntegerField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    status = models.CharField(max_length=255)
    fos_user_user = models.ForeignKey('FosUserUser', on_delete=models.RESTRICT, related_name='challenge_invites')

    class Meta:
        db_table = 'member_challenge_invite'


class MemberDeviceToken(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(null=True)
    api_key_id = models.IntegerField(null=True)
    is_deleted = models.BooleanField(default=False)
    modifiedby = models.IntegerField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    device_type = models.CharField(max_length=10)
    device_token = models.TextField(null=True)
    is_login = models.BooleanField()
    build = models.CharField(max_length=100, null=True)
    version = models.CharField(max_length=100, null=True)
    identifier_key = models.CharField(max_length=255, null=True)
    fos_user_user = models.ForeignKey('FosUserUser', on_delete=models.RESTRICT, related_name='device_tokens')

    class Meta:
        db_table = 'member_device_token'


class MemberKey(models.Model):
    id = models.AutoField(primary_key=True)
    member_id = models.IntegerField(null=True)
    key_id = models.IntegerField(null=True)
    created = models.DateTimeField()
    fos_user_user = models.ForeignKey('FosUserUser', on_delete=models.RESTRICT, related_name='member_keys')

    class Meta:
        db_table = 'member_key'


class MemberMeasurement(models.Model):
    id = models.AutoField(primary_key=True)
    member_id = models.IntegerField(null=True)
    is_deleted = models.BooleanField(default=False)
    modifiedby = models.IntegerField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    point = models.IntegerField()
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    height = models.DecimalField(max_digits=10, decimal_places=2)
    waist = models.DecimalField(max_digits=10, decimal_places=2)
    thighs = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    hips = models.DecimalField(max_digits=10, decimal_places=2)
    chest = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    isCurrent = models.BooleanField(null=True)
    image_name = models.CharField(max_length=255, null=True)
    wrist = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    forearm = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    fos_user_user = models.ForeignKey('FosUserUser', on_delete=models.RESTRICT, related_name='member_measurements')

    class Meta:
        db_table = 'member_measurement'


class MemberPackage(models.Model):
    id = models.AutoField(primary_key=True)
    member_id = models.IntegerField(null=True)
    is_deleted = models.BooleanField(default=False)
    modifiedby = models.IntegerField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    checkin = models.IntegerField(default=0)
    card_id = models.CharField(max_length=100, null=True)
    is_promotion = models.BooleanField(default=False)
    fos_user_user = models.ForeignKey('FosUserUser', on_delete=models.RESTRICT, null=True,
                                      related_name='member_packages')

    class Meta:
        db_table = 'member_package'


class MemberPromotionClicks(models.Model):
    id = models.AutoField(primary_key=True)
    member_id = models.IntegerField()
    promotion_id = models.IntegerField()
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    clicks = models.BigIntegerField(default=0)
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    fos_user_user = models.ForeignKey('FosUserUser', on_delete=models.RESTRICT)

    class Meta:
        db_table = 'member_promotion_clicks'


class MemberScheduleActivity(models.Model):
    id = models.AutoField(primary_key=True)
    member_id = models.IntegerField(null=True)
    schedule_detail_id = models.IntegerField(null=True)
    package_id = models.IntegerField()
    is_deleted = models.BooleanField(null=True)
    modifiedby = models.IntegerField()
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now=True)
    checkin = models.IntegerField()
    is_favourite = models.BooleanField()
    STATUS_CHOICES = [
        ('BOOKED', 'booked'),
        ('FAVOURITE', 'favourite'),
        ('CANCELLED', 'cancelled'),
        ('Expired', 'expired'),
        ('RESERVED', 'reserved'),
    ]
    STATUS = models.CharField(max_length=255, choices=STATUS_CHOICES, null=True)
    reminder = models.BooleanField(null=True)
    member_type = models.CharField(max_length=255, default='ForMe')
    fos_user_user = models.ForeignKey('FosUserUser', on_delete=models.RESTRICT, null=True,
                                      related_name='member_schedule_activities')
    member_package = models.ForeignKey('MemberPackage', on_delete=models.RESTRICT, null=True,
                                       related_name='member_schedule_activities')

    class Meta:
        db_table = 'member_schedule_activity'


class MemberWorkout(models.Model):
    id = models.AutoField(primary_key=True)
    member_id = models.IntegerField(null=True)
    key_id = models.IntegerField()
    is_deleted = models.BooleanField(default=False)
    modifiedby = models.IntegerField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    is_favourite = models.BooleanField(null=True)
    is_history = models.BooleanField(default=False)
    corporate_key = models.ForeignKey('CorporateKey', on_delete=models.CASCADE, null=True)
    fos_user_user = models.ForeignKey('FosUserUser', on_delete=models.RESTRICT, null=True)
    workout = models.ForeignKey('Workout', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'member_workout'


class ProfileKey(models.Model):
    id = models.AutoField(primary_key=True)
    company_id = models.IntegerField(null=True)
    is_deleted = models.BooleanField(default=False)
    modifiedby = models.IntegerField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    code = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    expire_date = models.DateTimeField(null=True)
    is_default = models.BooleanField(default=False)
    fos_user_user = models.ForeignKey('FosUserUser', on_delete=models.RESTRICT, related_name='profile_key', null=True)

    class Meta:
        db_table = 'profile_key'


class UserAwardPoint(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(null=True)
    is_deleted = models.BooleanField(default=False)
    modifiedby = models.IntegerField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    points_on_award = models.IntegerField()
    total_points = models.IntegerField()
    award_date_time = models.DateTimeField()
    fos_user_user = models.ForeignKey('FosUserUser', on_delete=models.RESTRICT, related_name='user_award_point',
                                      null=True)

    class Meta:
        db_table = 'user_award_point'


class UserCompany(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(null=True)
    company_id = models.IntegerField(null=True)
    is_deleted = models.BooleanField(default=False)
    modifiedby = models.IntegerField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    role = models.CharField(max_length=255)
    fos_user_user_fos_user_userTouser_company_company_id = models.ForeignKey('FosUserUser', on_delete=models.RESTRICT,
                                                                             related_name='user_company_company_id',
                                                                             null=True)
    fos_user_user_fos_user_userTouser_company_user_id = models.ForeignKey('FosUserUser', on_delete=models.RESTRICT,
                                                                          related_name='user_company_user_id',
                                                                          null=True)

    class Meta:
        db_table = 'user_company'


class UserDocuments(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(null=True)
    is_deleted = models.BooleanField(default=False)
    modifiedby = models.IntegerField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    documentName = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)
    fos_user_user = models.ForeignKey('FosUserUser', on_delete=models.RESTRICT, related_name='user_documents',
                                      null=True)

    class Meta:
        db_table = 'user_documents'


class UserProfileCategory(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    profilecategory_id = models.IntegerField()
    fos_user_user = models.ForeignKey('FosUserUser', on_delete=models.CASCADE, related_name='user_profile_category')

    class Meta:
        db_table = 'user_profilecategory'


class UserSaveCardTracking(models.Model):
    id = models.AutoField(primary_key=True)
    member_id = models.IntegerField(null=True)
    is_deleted = models.BooleanField(default=False)
    modifiedby = models.IntegerField()
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    save_card_tracking_id = models.CharField(max_length=255, null=True)
    last_four = models.CharField(max_length=255, null=True)
    payment_gateway_used = models.CharField(max_length=255, null=True)
    card_holder_name = models.CharField(max_length=255, null=True)
    card_type = models.CharField(max_length=255, null=True)
    fos_user_user = models.ForeignKey('FosUserUser', on_delete=models.RESTRICT, related_name='user_save_card_trackings')

    class Meta:
        db_table = 'user_save_card_tracking'


class Workout(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(null=True)
    workout_type = models.IntegerField(null=True)
    level_id = models.IntegerField(null=True)
    is_deleted = models.BooleanField(default=False)
    modifiedby = models.IntegerField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    image_name = models.CharField(max_length=255, null=True)
    background_music = models.CharField(max_length=100, null=True)
    duration = models.CharField(max_length=255, null=True)
    point = models.IntegerField(null=True)
    is_recommended = models.BooleanField(null=True)
    name_ar = models.TextField(null=True)
    description_ar = models.TextField(null=True)
    workout_level = models.ForeignKey('WorkoutLevel', on_delete=models.CASCADE, related_name='workouts', null=True)
    fos_user_user = models.ForeignKey('FosUserUser', on_delete=models.RESTRICT, related_name='workouts', null=True)
    workout_type_workoutToworkout_type = models.ForeignKey('WorkoutType', on_delete=models.CASCADE,
                                                           related_name='workouts', null=True)

    class Meta:
        db_table = 'workout'


class WorkoutLevel(models.Model):
    id = models.AutoField(primary_key=True)
    is_deleted = models.BooleanField(default=False)
    modifiedby = models.IntegerField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    point = models.IntegerField()
    image_name = models.CharField(max_length=255, blank=True, null=True)
    name_ar = models.TextField(blank=True, null=True)
    description_ar = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'workout_level'


class WorkoutType(models.Model):
    id = models.AutoField(primary_key=True)
    is_deleted = models.BooleanField(default=False)
    modifiedby = models.IntegerField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    name = models.CharField(max_length=100, db_column='name')
    code = models.CharField(max_length=100, db_column='code')
    description = models.TextField(blank=True, null=True)
    sequence = models.IntegerField()
    image_name = models.CharField(max_length=255, blank=True, null=True)
    name_ar = models.TextField(blank=True, null=True)
    description_ar = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'workout_type'


class CorporateDomains(models.Model):
    id = models.AutoField(primary_key=True)
    domain = models.CharField(max_length=255)
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'corporate_domains'


# Gamification
class GamificationPoint(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    assign_date = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey('FosUserUser', on_delete=models.CASCADE)
    gamification_point_type = models.ForeignKey('GamificationPointType', on_delete=models.CASCADE)

    class Meta:
        db_table = 'gamification_point'


class GamificationPointType(models.Model):
    id = models.AutoField(primary_key=True)
    points = models.IntegerField()
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'gamification_point_type'


class GamificationCorePointRecord(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    assign_date = models.DateTimeField(blank=True, null=True)
    log_activity = models.IntegerField(default=0, null=True)
    booking = models.IntegerField(default=0, null=True)
    step = models.IntegerField(default=0, null=True)
    heart_rate = models.IntegerField(default=0, null=True)
    ondemand = models.IntegerField(default=0, null=True)
    day_core_point = models.IntegerField(default=0, null=True)
    total_core_point = models.IntegerField(default=0, null=True)
    user = models.ForeignKey('FosUserUser', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'gamification_core_point_record'


class GamificationChallenge(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    logo = models.CharField(max_length=255, blank=True, null=True)
    cover_photo = models.CharField(max_length=255, blank=True, null=True)
    slug_url = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    description = models.TextField()
    status = models.CharField(max_length=180, blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_default = models.BooleanField(default=False)
    corporate_user = models.ForeignKey('FosUserUser', on_delete=models.CASCADE, blank=True, null=True)
    user_gamification_challenge = models.ManyToManyField('UserGamificationChallenge')
    group = models.ForeignKey('Groups', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'gamification_challenge'


class Groups(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=180, null=True, blank=True)
    logo = models.CharField(max_length=255, null=True, blank=True)
    cover_photo = models.CharField(max_length=255, null=True, blank=True)
    created_date = models.DateTimeField(null=True, blank=True)
    group_type = models.CharField(max_length=180, null=True, blank=True)
    privacy = models.CharField(max_length=255)
    is_deleted = models.BooleanField(default=False)
    company = models.ForeignKey('FosUserUser', on_delete=models.CASCADE, null=True, blank=True)
    is_cod_official = models.BooleanField(default=False)
    STATUS_CHOICES = (
        ('Active', 'active'),
        ('Inactive', 'inactive'),
    )
    status = models.CharField(max_length=180, null=True, blank=True, choices=STATUS_CHOICES, default='Active')
    user = models.ManyToManyField('UserGroups', related_name='groups')
    group_invites = models.ManyToManyField('GroupInvites', related_name='groups')

    class Meta:
        db_table = 'groups'


class GroupInvites(models.Model):
    id = models.AutoField(primary_key=True)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)
    group_invited_user = models.ForeignKey('FosUserUser', related_name='group_invited_user', on_delete=models.CASCADE)
    group_invited_by_user = models.ForeignKey('FosUserUser', related_name='group_invited_by_user',
                                              on_delete=models.CASCADE)
    status = models.CharField(max_length=180)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'group_invites'


class UserGroups(models.Model):
    id = models.AutoField(primary_key=True)
    STATUS_CHOICES = (
        ('accepted', 'Accepted'),
        ('pending', 'Pending'),
        ('rejected', 'Rejected'),
    )
    user = models.ForeignKey('FosUserUser', on_delete=models.CASCADE)
    group = models.ForeignKey('Groups', on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='accepted')

    class Meta:
        db_table = 'user_groups'


class UserGamificationChallenge(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('FosUserUser', on_delete=models.CASCADE)
    rank = models.IntegerField(default=0, null=True)
    gamification_challenge_id = models.IntegerField()

    class Meta:
        db_table = 'user_gamification_challenge'


class FosUserUser(models.Model):
    id = models.AutoField(primary_key=True)
    parent_id = models.IntegerField(null=True)
    username = models.CharField(max_length=180)
    profile_picture = models.CharField(max_length=255, null=True)
    access_token = models.CharField(max_length=255, null=True)
    username_canonical = models.CharField(max_length=180, unique=True)
    email = models.CharField(max_length=180)
    email_canonical = models.CharField(max_length=180, unique=True)
    enabled = models.BooleanField()
    salt = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=255)
    last_login = models.DateTimeField(null=True)
    confirmation_token = models.CharField(max_length=180, null=True, unique=True)
    password_requested_at = models.DateTimeField(null=True)
    roles = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    date_of_birth = models.DateTimeField(null=True)
    firstname = models.CharField(max_length=64, null=True)
    privacy = models.CharField(max_length=255, default="private", null=True)
    lastname = models.CharField(max_length=64, null=True)
    website = models.CharField(max_length=64, null=True)
    biography = models.CharField(max_length=1000, null=True)
    gender = models.CharField(max_length=1, null=True)
    locale = models.CharField(max_length=8, null=True)
    timezone = models.CharField(max_length=64, null=True)
    phone = models.CharField(max_length=64, null=True)
    facebook_uid = models.CharField(max_length=255, null=True)
    facebook_name = models.CharField(max_length=255, null=True)
    facebook_data = models.TextField(null=True)
    twitter_uid = models.CharField(max_length=255, null=True)
    twitter_name = models.CharField(max_length=255, null=True)
    twitter_data = models.TextField(null=True)
    gplus_uid = models.CharField(max_length=255, null=True)
    gplus_name = models.CharField(max_length=255, null=True)
    gplus_data = models.TextField(null=True)
    token = models.CharField(max_length=255, null=True)
    two_step_code = models.CharField(max_length=255, null=True)
    promotional_email_enable = models.BooleanField(null=True)
    corporate_email_enable = models.BooleanField(null=True)
    about_corporate = models.TextField(null=True)
    address = models.CharField(max_length=100, null=True)
    term_condition = models.CharField(max_length=255, null=True)
    is_gdpr = models.BooleanField(null=True)
    address_one = models.CharField(max_length=100, null=True)
    address_two = models.CharField(max_length=100, null=True)
    po_box = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    contact_title = models.CharField(max_length=100, null=True)
    contact_firstname = models.CharField(max_length=50, null=True)
    contact_lastname = models.CharField(max_length=50, null=True)
    designation = models.CharField(max_length=50, null=True)
    contact_email = models.CharField(max_length=50, null=True)
    contact_no = models.CharField(max_length=100, null=True)
    contact_url = models.CharField(max_length=100, null=True)
    notes = models.CharField(max_length=255, null=True)
    company_logo = models.CharField(max_length=255, null=True)
    company_name = models.CharField(max_length=100, null=True)
    latitude = models.CharField(max_length=255, null=True)
    longitude = models.CharField(max_length=255, null=True)
    card_id = models.CharField(max_length=100, null=True)
    notification = models.BooleanField(null=True)
    enable_discount = models.BooleanField(null=True)
    is_profile_completed = models.BooleanField(default=False)
    step_count = models.IntegerField(null=True)
    distance = models.FloatField(null=True)
    step_date_time = models.DateTimeField(null=True)
    last_reward_steps = models.IntegerField(null=True)
    is_deleted = models.IntegerField(default=0)
    apple_id = models.CharField(max_length=255, null=True)
    company_banner = models.CharField(max_length=255, null=True)
    appVersion_id = models.IntegerField(null=True)
    is_onboarded = models.BooleanField(default=False)
    is_app_user = models.BooleanField(default=False)
    cognito_username = models.CharField(max_length=255, null=True)
    is_pushed = models.JSONField(null=True)
    temp_auth = models.CharField(max_length=1000, null=True)
    is_forced_logout = models.BooleanField(default=False)
    stripe_customer_id = models.CharField(max_length=255, null=True)
    garmin_user_id = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'fos_user_user'
