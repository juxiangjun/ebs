from django.db import models

class RptItem(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=24, blank=True)
    name = models.CharField(max_length=192, blank=True)
    rpt_type_id = models.IntegerField(null=True, blank=True)
    rpt_type_code = models.CharField(max_length=12, blank=True)
    rpt_type_name = models.CharField(max_length=96, blank=True)
    class Meta:
        db_table = u'rpt_item'

class RptItemCopy(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=24, blank=True)
    name = models.CharField(max_length=192, blank=True)
    rpt_type_id = models.IntegerField(null=True, blank=True)
    rpt_type_code = models.CharField(max_length=12, blank=True)
    rpt_type_name = models.CharField(max_length=96, blank=True)
    class Meta:
        db_table = u'rpt_item_copy'

class RptMetric(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=24, blank=True)
    name = models.CharField(max_length=192, blank=True)
    parent_id = models.CharField(max_length=12, blank=True)
    is_rpt = models.IntegerField(null=True, blank=True)
    years = models.CharField(max_length=24, blank=True)
    formular = models.TextField(blank=True)
    comments = models.CharField(max_length=768, blank=True)
    used_items = models.CharField(max_length=768, blank=True)
    fixed_items = models.CharField(max_length=768, blank=True)
    value_items = models.TextField(blank=True)
    measurement_interval = models.TextField(blank=True)
    status = models.CharField(max_length=6, blank=True)
    shift_to_previous_year = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'rpt_metric'

class RptType(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=12, blank=True)
    short_name = models.CharField(max_length=48, blank=True)
    full_name = models.CharField(max_length=192, blank=True)
    columns = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'rpt_type'

class StkDividend(models.Model):
    id = models.CharField(max_length=108, primary_key=True)
    stock_code = models.CharField(max_length=24, blank=True)
    stock_name = models.CharField(max_length=192, blank=True)
    register_date = models.DateField(null=True, blank=True)
    stock_count = models.FloatField(null=True, blank=True)
    trans_date = models.DateField(null=True, blank=True)
    end_value = models.FloatField(null=True, blank=True)
    trans_value = models.FloatField(null=True, blank=True)
    unit_tax = models.FloatField(null=True, blank=True)
    unit_no_tax = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=3, blank=True)
    created_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'stk_dividend'

class StkInfo(models.Model):
    id = models.CharField(max_length=108, primary_key=True)
    code = models.CharField(max_length=24)
    name = models.CharField(max_length=48)
    created_time = models.DateTimeField(null=True, blank=True)
    rpt_last_updated_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'stk_info'

class StkMainCategory(models.Model):
    id = models.CharField(max_length=108, primary_key=True)
    code = models.CharField(max_length=24, blank=True)
    name = models.CharField(max_length=384, blank=True)
    class Meta:
        db_table = u'stk_main_category'

class StkProfile(models.Model):
    id = models.CharField(max_length=108, blank=True)
    stock_id = models.CharField(max_length=108, blank=True)
    stock_code = models.CharField(max_length=24, blank=True)
    stock_name = models.CharField(max_length=96, blank=True)
    ab_code = models.CharField(max_length=96, blank=True)
    issued_date = models.DateField(null=True, blank=True)
    transferable = models.CharField(max_length=192, blank=True)
    short_name = models.CharField(max_length=384, blank=True)
    full_name = models.CharField(max_length=768, blank=True)
    registration_addr = models.CharField(max_length=768, blank=True)
    addr = models.CharField(max_length=768, blank=True)
    principal = models.CharField(max_length=96, blank=True)
    board_secretary = models.CharField(max_length=96, blank=True)
    email = models.CharField(max_length=192, blank=True)
    tel = models.CharField(max_length=72, blank=True)
    web_site = models.CharField(max_length=192, blank=True)
    industry = models.CharField(max_length=192, blank=True)
    sse_industry = models.CharField(max_length=192, blank=True)
    province = models.CharField(max_length=96, blank=True)
    ab_status = models.CharField(max_length=24, blank=True)
    is_sample = models.CharField(max_length=24, blank=True)
    overseas_listing = models.CharField(max_length=24, blank=True)
    overseas_addr = models.CharField(max_length=768, blank=True)
    created_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'stk_profile'

class StkTransData(models.Model):
    id = models.CharField(max_length=108, primary_key=True)
    stock_code = models.CharField(max_length=24, blank=True)
    stock_name = models.CharField(max_length=192, blank=True)
    seq = models.IntegerField(null=True, blank=True)
    trans_date = models.DateField(null=True, blank=True)
    end_value = models.FloatField(null=True, blank=True)
    start_value = models.FloatField(null=True, blank=True)
    max_value = models.FloatField(null=True, blank=True)
    min_value = models.FloatField(null=True, blank=True)
    current = models.FloatField(null=True, blank=True)
    price_offset = models.FloatField(null=True, blank=True)
    price_ratio = models.FloatField(null=True, blank=True)
    total = models.FloatField(null=True, blank=True)
    total_offset = models.FloatField(null=True, blank=True)
    total_ratio = models.FloatField(null=True, blank=True)
    qty = models.IntegerField(null=True, blank=True)
    qty_offset = models.FloatField(null=True, blank=True)
    qty_ratio = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=3, blank=True)
    created_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'stk_trans_data'

class UsrMetric(models.Model):
    id = models.IntegerField(primary_key=True)
    usr_id = models.IntegerField(null=True, blank=True)
    cfs_metric_id = models.IntegerField(null=True, blank=True)
    cfs_metric_code = models.CharField(max_length=12, blank=True)
    cfs_metric_name = models.CharField(max_length=384, blank=True)
    metric_values = models.TextField(blank=True)
    measurement_interval = models.TextField(blank=True)
    class Meta:
        db_table = u'usr_metric'

class UsrRptData(models.Model):
    id = models.CharField(max_length=108, primary_key=True)
    stock_code = models.IntegerField(null=True, blank=True)
    rpt_item_code = models.CharField(max_length=24, blank=True)
    rpt_item_name = models.CharField(max_length=192, blank=True)
    rpt_type_code = models.CharField(max_length=12, blank=True)
    q1 = models.TextField(blank=True)
    q2 = models.TextField(blank=True)
    q3 = models.TextField(blank=True)
    q4 = models.TextField(blank=True)
    class Meta:
        db_table = u'usr_rpt_data'

