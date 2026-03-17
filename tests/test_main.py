### === test_models.py ===
```python
import unittest
from django.test import TestCase
from .models import Product, Category, Brand

class TestProductModel(TestCase):
    def test_product_creation(self):
        product = Product.objects.create(
            name='Test Product',
            description='Test product description',
            price=10.99,
            category=Category.objects.create(name='Test Category'),
            brand=Brand.objects.create(name='Test Brand')
        )
        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(product.description, 'Test product description')
        self.assertEqual(product.price, 10.99)

class TestCategoryModel(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(name='Test Category')
        self.assertEqual(category.name, 'Test Category')

class TestBrandModel(TestCase):
    def test_brand_creation(self):
        brand = Brand.objects.create(name='Test Brand')
        self.assertEqual(brand.name, 'Test Brand')
```

### === test_views.py ===
```python
import unittest
from django.test import TestCase, Client
from django.urls import reverse
from .models import Product, Category, Brand

class TestProductViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.product = Product.objects.create(
            name='Test Product',
            description='Test product description',
            price=10.99,
            category=Category.objects.create(name='Test Category'),
            brand=Brand.objects.create(name='Test Brand')
        )

    def test_product_list_view(self):
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_list.html')

    def test_product_detail_view(self):
        response = self.client.get(reverse('product_detail', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_detail.html')

class TestCategoryViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name='Test Category')

    def test_category_list_view(self):
        response = self.client.get(reverse('category_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category_list.html')

    def test_category_detail_view(self):
        response = self.client.get(reverse('category_detail', args=[self.category.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category_detail.html')

class TestBrandViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.brand = Brand.objects.create(name='Test Brand')

    def test_brand_list_view(self):
        response = self.client.get(reverse('brand_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'brand_list.html')

    def test_brand_detail_view(self):
        response = self.client.get(reverse('brand_detail', args=[self.brand.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'brand_detail.html')
```

### === test_forms.py ===
```python
import unittest
from django.test import TestCase
from .forms import ProductForm, CategoryForm, BrandForm

class TestProductForm(TestCase):
    def test_product_form_valid(self):
        form_data = {
            'name': 'Test Product',
            'description': 'Test product description',
            'price': 10.99,
            'category': 1,
            'brand': 1
        }
        form = ProductForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_product_form_invalid(self):
        form_data = {
            'name': '',
            'description': 'Test product description',
            'price': 10.99,
            'category': 1,
            'brand': 1
        }
        form = ProductForm(data=form_data)
        self.assertFalse(form.is_valid())

class TestCategoryForm(TestCase):
    def test_category_form_valid(self):
        form_data = {
            'name': 'Test Category'
        }
        form = CategoryForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_category_form_invalid(self):
        form_data = {
            'name': ''
        }
        form = CategoryForm(data=form_data)
        self.assertFalse(form.is_valid())

class TestBrandForm(TestCase):
    def test_brand_form_valid(self):
        form_data = {
            'name': 'Test Brand'
        }
        form = BrandForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_brand_form_invalid(self):
        form_data = {
            'name': ''
        }
        form = BrandForm(data=form_data)
        self.assertFalse(form.is_valid())
```

### === test_urls.py ===
```python
import unittest
from django.test import TestCase
from django.urls import reverse

class TestUrls(TestCase):
    def test_product_list_url(self):
        url = reverse('product_list')
        self.assertEqual(url, '/products/')

    def test_product_detail_url(self):
        url = reverse('product_detail', args=[1])
        self.assertEqual(url, '/products/1/')

    def test_category_list_url(self):
        url = reverse('category_list')
        self.assertEqual(url, '/categories/')

    def test_category_detail_url(self):
        url = reverse('category_detail', args=[1])
        self.assertEqual(url, '/categories/1/')

    def test_brand_list_url(self):
        url = reverse('brand_list')
        self.assertEqual(url, '/brands/')

    def test_brand_detail_url(self):
        url = reverse('brand_detail', args=[1])
        self.assertEqual(url, '/brands/1/')
```

### === test_templates.py ===
```python
import unittest
from django.test import TestCase
from django.template import Template

class TestTemplates(TestCase):
    def test_product_list_template(self):
        template = Template('{% extends "base.html" %}{% block content %}Product List{% endblock %}')
        self.assertTemplateUsed(template, 'base.html')

    def test_product_detail_template(self):
        template = Template('{% extends "base.html" %}{% block content %}Product Detail{% endblock %}')
        self.assertTemplateUsed(template, 'base.html')

    def test_category_list_template(self):
        template = Template('{% extends "base.html" %}{% block content %}Category List{% endblock %}')
        self.assertTemplateUsed(template, 'base.html')

    def test_category_detail_template(self):
        template = Template('{% extends "base.html" %}{% block content %}Category Detail{% endblock %}')
        self.assertTemplateUsed(template, 'base.html')

    def test_brand_list_template(self):
        template = Template('{% extends "base.html" %}{% block content %}Brand List{% endblock %}')
        self.assertTemplateUsed(template, 'base.html')

    def test_brand_detail_template(self):
        template = Template('{% extends "base.html" %}{% block content %}Brand Detail{% endblock %}')
        self.assertTemplateUsed(template, 'base.html')
```

### === test_api.py ===
```python
import unittest
from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Product, Category, Brand

class TestProductAPI(APITestCase):
    def test_product_list_api(self):
        product = Product.objects.create(
            name='Test Product',
            description='Test product description',
            price=10.99,
            category=Category.objects.create(name='Test Category'),
            brand=Brand.objects.create(name='Test Brand')
        )
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_product_detail_api(self):
        product = Product.objects.create(
            name='Test Product',
            description='Test product description',
            price=10.99,
            category=Category.objects.create(name='Test Category'),
            brand=Brand.objects.create(name='Test Brand')
        )
        response = self.client.get(f'/api/products/{product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Test Product')

class TestCategoryAPI(APITestCase):
    def test_category_list_api(self):
        category = Category.objects.create(name='Test Category')
        response = self.client.get('/api/categories/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_category_detail_api(self):
        category = Category.objects.create(name='Test Category')
        response = self.client.get(f'/api/categories/{category.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Test Category')

class TestBrandAPI(APITestCase):
    def test_brand_list_api(self):
        brand = Brand.objects.create(name='Test Brand')
        response = self.client.get('/api/brands/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_brand_detail_api(self):
        brand = Brand.objects.create(name='Test Brand')
        response = self.client.get(f'/api/brands/{brand.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Test Brand')
```

### === test_authentication.py ===
```python
import unittest
from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

class TestAuthentication(APITestCase):
    def test_user_registration(self):
        user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword'
        }
        response = self.client.post('/api/register/', user_data)
        self.assertEqual(response.status_code, 201)

    def test_user_login(self):
        user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )
        login_data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post('/api/login/', login_data)
        self.assertEqual(response.status_code, 200)
```

### === test_payment.py ===
```python
import unittest
from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from .models import Order, Payment

class TestPayment(APITestCase):
    def test_payment_processing(self):
        user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )
        order = Order.objects.create(
            user=user,
            total=10.99
        )
        payment_data = {
            'order_id': order.id,
            'payment_method': 'credit_card',
            'payment_status': 'paid'
        }
        response = self.client.post('/api/payments/', payment_data)
        self.assertEqual(response.status_code, 201)

    def test_payment_status_update(self):
        user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )
        order = Order.objects.create(
            user=user,
            total=10.99
        )
        payment = Payment.objects.create(
            order=order,
            payment_method='credit_card',
            payment_status='pending'
        )
        payment_data = {
            'payment_status': 'paid'
        }
        response = self.client.patch(f'/api/payments/{payment.id}/', payment_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['payment_status'], 'paid')
```