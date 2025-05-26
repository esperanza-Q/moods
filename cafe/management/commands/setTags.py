from django.core.management.base import BaseCommand
from cafe.models import Tag  # your_app을 실제 앱 이름으로 바꾸세요!

class Command(BaseCommand):
    help = "Create initial Tag objects with code and label"

    def handle(self, *args, **kwargs):
        codes = [
            "coffee", "refined", "together", "dessert",
            "clean", "study", "cozy", "big",
            "alone", "cuty", "always", "picture"
        ]
        labels = [
            "#커피가 맛있는",
            "#세련된",
            "#단체모임하기 좋은",
            "#디저트가 맛있는",
            "#깔끔한",
            "#카공하기 좋은",
            "#포근한",
            "#넓은",
            "#혼자 있기 좋은",
            "#아기자기한",
            "#24시간 영업하는",
            "#사진 찍기 좋은",
        ]

        for code, label in zip(codes, labels):
            tag, created = Tag.objects.get_or_create(code=code, defaults={'label': label})
            if not created:
                tag.label = label
                tag.save()
            self.stdout.write(f"{'Created' if created else 'Updated'} Tag: code={code}, label={label}")