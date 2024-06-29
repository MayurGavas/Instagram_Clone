from rest_framework.serializers import ModelSerializer
from .models import Post,MediaHandeling


class Mediafileserializer(ModelSerializer):

    class Meta:
        model = MediaHandeling
        fields = ['seq_no','media_file','media_under_post']

class AllPostView(ModelSerializer):
    class Meta:
        model = Post
        fields = ['caption_heading','caption_text','posted_by','is_published','location',]


class FullPostDetailsWithMediaSerialiser(ModelSerializer):
    media = Mediafileserializer(source=Post.posted_by,many=True)
    # source=Post.posted_by,

    class Meta:
        model = Post
        fields = ['caption_heading','caption_text','posted_by','location','media']


"""
    def create(self, validated_data):
        media_data = validated_data.pop()
        post = Post.objects.create(**validated_data)
        for media_item in media_data:
            MediaHandeling.objects.create(media_under_post=post,**media_item)
        return post
"""
