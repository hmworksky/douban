from django.db import models
from datetime import datetime
# Create your models here.


class BookCategory(models.Model):
    """
        书籍类别
    """
    CATEGORY_TYPE = (
        (1, "一级类目"),
        (2, "二级类目"),
        (3, "三级类目"),
        (4, "四级类目"),
    )
    name = models.CharField(max_length=50, default="", verbose_name="类别名", help_text="类别名")
    code = models.CharField(max_length=50, default="", verbose_name="类别code", help_text="类别code")
    desc = models.CharField(max_length=100, default="", verbose_name="类别描述", help_text="类别描述")
    category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="类目级别", help_text="类目级别")
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="父类目级别", help_text="父目录",
                                        related_name="sub_cat", on_delete=models.CASCADE)
    is_tab = models.BooleanField(default=False, verbose_name="是否导航", help_text="是否导航")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "书籍类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class BookAuthor(models.Model):
    """
        书籍作者
    """
    name = models.CharField(max_length=100, default="", verbose_name="名字")
    country = models.CharField(max_length=20, default="", verbose_name="国家")
    docs = models.CharField(max_length=2500, default="", verbose_name="简介", help_text="简介")
    representative_work = models.CharField(max_length=100, default="", verbose_name="代表作", help_text="代表作")

    class Meta:
        verbose_name = "作者信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class PublishInformation(models.Model):
    """
        出版社
    """
    author = models.ForeignKey(BookAuthor, max_length=100, default="", verbose_name="作者", help_text="作者",
                               on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="", verbose_name="出版社", help_text="出版社")
    original_name = models.CharField(max_length=50, default="", verbose_name="原作名", help_text="原作名")
    translator = models.CharField(max_length=50, default="", verbose_name="译者", help_text="译者")
    publication_year = models.DateField(default="", verbose_name="出版年", help_text="出版年")
    page_num = models.IntegerField(default=0, verbose_name="页数", help_text="页数")
    price = models.FloatField(default=0, verbose_name="定价", help_text="定价")
    Binding = models.CharField(max_length=20, default="平装", verbose_name="装帧类型", help_text="装帧类型")
    isbn = models.CharField(max_length=50, default="", verbose_name="ISBN", help_text="ISBN")

    class Meta:
        verbose_name = "出版社信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Books(models.Model):
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE, verbose_name="书籍类目", help_text="书籍类目")
    book_sn = models.CharField(max_length=100, default="", verbose_name="书籍唯一编号", help_text="书籍唯一编号")
    name = models.CharField(max_length=50, verbose_name="书籍名字", help_text="书籍名字")
    goods_front_image = models.ImageField(upload_to="books/images/", null=True, blank=True, verbose_name="封面图",
                                          help_text="封面图")
    publish_information = models.ForeignKey(PublishInformation, on_delete=models.CASCADE, verbose_name="出版信息",
                                            help_text="出版信息")
    author = models.ForeignKey(BookAuthor, verbose_name="作者", help_text="作者", on_delete=models.CASCADE)
    docs = models.CharField(max_length=2500, default="", verbose_name="简介", help_text="简介")
    is_new = models.BooleanField(default=False, verbose_name="是否新品")
    is_hot = models.BooleanField(default=False, verbose_name="是否热销")
    price = models.FloatField(default=0, verbose_name="售价", help_text="售价")
    add_time = models.DateTimeField(verbose_name="添加时间", auto_now_add=True)
    update_time = models.DateTimeField(verbose_name="更新时间", auto_now=True)

    class Meta:
        verbose_name = "书籍信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class BookDetail(models.Model):
    CHAPTER_TYPE = (
        (1, "章节标题"),
        (2, "章节内容")
    )

    book = models.ForeignKey(Books, on_delete=models.CASCADE, verbose_name="书籍ID")
    chapter_number = models.IntegerField(default=0, unique=True, verbose_name="章节编号")
    docs = models.CharField(choices=CHAPTER_TYPE, default="", max_length=100, verbose_name="章节类型")

    class Meta:
        verbose_name = "书籍信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.book





