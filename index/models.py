from django.db import models

from wagtail.models import Page, Orderable
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from modelcluster.models import ParentalKey
# from wagtail.core.models import Orderable



class CarouselImage(Orderable):
    page = ParentalKey('IndexPage', on_delete=models.CASCADE, related_name='carousel_images', )
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+', null=True, blank=True,
    )
    caption = models.CharField(blank=True, max_length=250)
    description = models.CharField(blank=True, max_length=300)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
        FieldPanel('description'),
    ]



class IndexPage(Page):
    header_image = models.ForeignKey("wagtailimages.image", on_delete=models.SET_NULL, null=True, blank=True, related_name="+")
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                InlinePanel('carousel_images', label="Carousel Images", max_num=3, min_num=1)
                ],
                heading="Carousel Images", 
        ),
        FieldPanel("header_image",),

    ]