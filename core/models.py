from django.db import models

class Newsletter(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['-subscribed_at']
        verbose_name = 'Newsletter Subscriber'
        verbose_name_plural = 'Newsletter Subscribers'


class ContactSubmission(models.Model):
    SUBJECT_CHOICES = [
        ('general', 'General Inquiry'),
        ('manufacturing', 'Manufacturing Services'),
        ('installation', 'Installation & Commissioning'),
        ('calibration', 'Calibration & Testing'),
        ('repair', 'Repair & Maintenance'),
        ('amc', 'Annual Maintenance Contract'),
        ('custom', 'Custom Development'),
        ('partnership', 'Partnership Opportunity'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES)
    message = models.TextField()
    agree_terms = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.subject}"

    class Meta:
        ordering = ['-submitted_at']
        verbose_name = 'Contact Submission'
        verbose_name_plural = 'Contact Submissions'


class ServiceInquiry(models.Model):
    SERVICE_CHOICES = [
        ('Manufacturing', 'Manufacturing'),
        ('Sales & Distribution', 'Sales & Distribution'),
        ('Installation', 'Installation & Commissioning'),
        ('Calibration', 'Calibration & Testing'),
        ('Repair', 'Repair & Maintenance'),
        ('AMC', 'Annual Maintenance Contracts'),
        ('Custom', 'Custom Equipment Development'),
    ]

    service_name = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.customer_name} - {self.service_name}"

    class Meta:
        ordering = ['-submitted_at']
        verbose_name = 'Service Inquiry'
        verbose_name_plural = 'Service Inquiries'


class Customer(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='customers/logos/')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
