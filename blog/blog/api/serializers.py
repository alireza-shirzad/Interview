from venv import create
from rest_framework import serializers
from ..models import Post, Rating
from django.db.models import Q

class PostSerializer(serializers.ModelSerializer):
    userRating = serializers. SerializerMethodField()

    def get_userRating(self, obj):
        userId = int(self.context.get('request').query_params.get('user', None))
        if userId:
            rating = Rating.objects.filter(Q(user=userId) & Q(post_id=obj.id)).first()
            if rating:
                return rating.rating
        return None

    class Meta:
        model = Post
        fields = '__all__'
    

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

    def validate_rating(self, value):
        if value < 0 or value >5 :
            raise serializers.ValidationError('Rating must be between 0 and 5')
        return value   

    def save(self, **kwargs):
        
        rating, created = Rating.objects.get_or_create(
            user_id=self._validated_data['user'].id,
            post_id=self._validated_data['post'].id,
            defaults={'rating': self._validated_data['rating']}
        )
        post = rating.post

        if created:
            post.ratingCount = post.ratingCount + 1
            post.averageRating = ((post.averageRating*(post.ratingCount-1))+rating.rating)/post.ratingCount
            print(post.ratingCount)
            print(post.averageRating)

        if not created:
            previousRating = rating.rating
            rating.rating = self._validated_data['rating']
            post.averageRating = ((post.averageRating*post.ratingCount)-previousRating+rating.rating)/post.ratingCount
            rating.save()
        
        post.save()


    
