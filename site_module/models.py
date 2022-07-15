from django.db import models


# Create your models here.

class SiteSetting(models.Model):
    site_name = models.CharField(max_length=200, verbose_name='نام سایت')
    site_url = models.CharField(max_length=200, verbose_name='دامنه سایت')
    address = models.CharField(max_length=200, verbose_name=' آدرس')
    phone = models.CharField(max_length=200, verbose_name='تلفن', null=True, blank=True)
    fax = models.CharField(max_length=200, verbose_name='فکس', null=True, blank=True)
    email = models.CharField(max_length=200, verbose_name='ایمیل', null=True, blank=True)
    copy_right = models.TextField(verbose_name='متن کپی رایت')
    about_us_text = models.TextField(verbose_name='متن درباره ما')
    site_logo = models.ImageField(upload_to='images/site-setting/', verbose_name='لوگو سایت')
    is_main_settings = models.BooleanField(verbose_name='تنظیملات اصلی')

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات سایت'


class FooterLinkBox(models.Model):
    title = models.CharField(max_length=202, verbose_name="عنوان")

    class Meta:
        verbose_name = ' دسته بندی لینک های فوتر'
        verbose_name_plural = ' دسته بندی های لینک های فوتر'

    def __str__(self):
        return self.title


class FooterLink(models.Model):
    title = models.CharField(max_length=202, verbose_name='عنوان')
    url = models.URLField(max_length=500, verbose_name='لینک')
    footer_link_box = models.ForeignKey(to=FooterLinkBox, verbose_name='دسته بندی', on_delete=models.CASCADE)

    class Meta:
        verbose_name = ' لینک فوتر'
        verbose_name_plural = ' لینک های فوتر'

    def __str__(self):
        return self.title


class Slider(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    description = models.CharField(max_length=200, verbose_name='توضیحات اسلایدر')
    url = models.URLField(max_length=500, verbose_name='لینک')
    url_title = models.CharField(max_length=500, verbose_name='عنوان لینک')
    image = models.ImageField(upload_to='images/site-setting/slider-images/', verbose_name='تصویر اسلایدر')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیر فعال')

    class Meta:
        verbose_name = 'تنظیمات اسلایدر'
        verbose_name_plural = 'تنظیمات اسلایدر ها'

    def __str__(self):
        return self.title


class SiteBanner(models.Model):
    class SiteBannerPositions(models.TextChoices):
        product_list = ("product_list", "صفحه لیست محصولات")

        product_detail = ("product_detail", "صفحه جزییات محصولات")

        article_page = ("article_page", "صفحه لیست مقالات")
        article_detail_page = ("article_detail_page", "صفحه مقاله")

        about_us = ('about_us', 'صفحه درباره ما')

    title = models.CharField(max_length=200, verbose_name='عنوان')
    url = models.URLField(max_length=200, null=True, blank=True, verbose_name='url')
    image = models.ImageField(upload_to='images/banner', verbose_name='تصویر')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')
    position = models.CharField(max_length=200, choices=SiteBannerPositions.choices, verbose_name='محل قرار گیری')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'بنر تبلیاتی'

        verbose_name_plural = 'بنر هی تبلیغاتی'
