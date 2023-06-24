from django.db import models
from django.core.exceptions import ValidationError


from wagtail.models import Page, Orderable
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from modelcluster.models import ParentalKey
from wagtail.snippets.models import register_snippet
from phonenumber_field.modelfields import PhoneNumberField





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


@register_snippet
class Header(models.Model):
    opening_hours = models.CharField(max_length=255)
    contact = PhoneNumberField(null=True)
    email = models.EmailField(null=True)
    logo = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+', null=True
    )
    home_url = models.URLField(null=True)


    panels =[
        MultiFieldPanel([
            FieldPanel('opening_hours'),
            FieldPanel('contact'),
            FieldPanel('email'),
            ],
            heading ="Header"


        ),
        MultiFieldPanel([
            FieldPanel('home_url'),
            FieldPanel('logo'),
        ],
        heading ="Nav Bar"
        )
    ]
    

    def clean(self):
        # Check if there is already an existing object in the model
        if Header.objects.exists() and not self.pk:
            raise ValidationError("Only one instance of Header is allowed.")

    def save(self, *args, **kwargs):
        self.clean()  # Validate the object before saving
        super().save(*args, **kwargs)
        

    def __str__(self):
        return "Header"
    
    class Meta:
        verbose_name_plural = "Header"
    

@register_snippet
class Footer(models.Model):
    footer_logo = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    home_url = models.URLField(null=True)
    contact = PhoneNumberField(null=True)
    email = models.EmailField(null=True)
    address = models.CharField(max_length=500, null=True)

    panels =[
        MultiFieldPanel([
            FieldPanel('home_url'),
            FieldPanel('footer_logo'),
            FieldPanel('contact'),
            FieldPanel('email'),
            FieldPanel('address'),

        ]
        )
    ]

    def clean(self):
        # Check if there is already an existing object in the model
        if Footer.objects.exists() and not self.pk:
            raise ValidationError("Only one instance of Footer is allowed.")

    def save(self, *args, **kwargs):
        self.clean()  # Validate the object before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return "Footer"
    
    class Meta:
        verbose_name_plural = "Footer"
    

