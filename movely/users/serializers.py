from rest_framework import routers, serializers, viewsets
from movely.users.models import *


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserPhoto
        fields = ('photo',)


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserVideo
        fields = ('video',)


class ProfileSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True)
    video = VideoSerializer()

    class Meta:
        model = UserProfile
        fields = ('id', 'school', 'major', 'job', 'company',
                  'personality', 'region', 'height', 'body_type', 'video', 'photo_ids', "photos")


class UserSerializer(serializers.ModelSerializer):
    # profiles = serializers.PrimaryKeyRelatedField(
    #     queryset=UserProfile.objects.filter(active=True), pk_field="user_id")
    # profiles = ProfileSerializer(many=True, read_only=True)
    profile = serializers.SerializerMethodField()
    #     queryset=UserProfile.objects.filter(active=True))

    def get_profile(self, object):
        qs = UserProfile.objects.filter(active=True).first()
        serializer = ProfileSerializer(instance=qs)
        return serializer.data

    class Meta:
        model = User
        # depth = 2
        fields = ('id', 'username', 'gender', 'birthday', 'point', 'heart', 'profile')