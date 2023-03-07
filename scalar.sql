-- app password = jmeejebnrpcvmvsc

product = Product.objects.get(id=1)
select * from Product where id=1

product=product.objects.filter(vendor = 'Adidas')
select * from product where vendor = 'Adidas'



seller = Reseller.objects.all()
select * from Reseller

data=Reseller.objects.values('title','img')
select title,img from Reseller 



products.objects.filter(id=pid).update(desc="sports shoe for mens",price=2999)
update products set desc="sports shoe for men",price=2999 where id=pid


Entry.objects.filter(pub_date__lte='2006-01-01') 
SELECT * FROM blog_entry WHERE pub_date <= '2006-01-01';


Entry.objects.get(headline__exact="Man bites dog") 
SELECT * from blog_entry WHERE headline = 'Man bites dog'; 


 Blog.objects.get(name__iexact="beatles blog")
 Would match a Blog titled “Beatles Blog”, “beatles blog”, or even “BeAtlES blOG”.


 Entry.objects.get(headline__contains='Lennon') 
 SELECT * from blog_entry WHERE headline LIKE '%Lennon%'; 
--  Note this will match the headline 'Today Lennon honored' but not 'today lennon honored'.



Entry.objects.get(headline__startwith='L') 
 SELECT * from blog_entry WHERE headline LIKE 'L%'; 


Entry.objects.get(headline__endwith='L') 
 SELECT * from blog_entry WHERE headline LIKE '%L';


q1.filter(pub_date__gte=datetime.date.today())
select ... where pub_date >= CURRENT_DATE;


 from django.db.models import Q
queryset = User.objects.filter(Q(first_name__startswith='R') | Q(last_name__startswith='D'))
<QuerySet [<User: Ricky>, <User: Ritesh>, <User: Radha>, <User: Raghu>, <User: rishab>]>



queryset = User.objects.filter(
    Q(first_name__startswith='R') & Q(last_name__startswith='D')
)
>>> queryset
<QuerySet [<User: Ricky>, <User: Ritesh>, <User: rishab>]>



SELECT "auth_user"."id",
       "auth_user"."password",
       "auth_user"."last_login",
       "auth_user"."is_superuser",
       "auth_user"."username",
       "auth_user"."first_name",
       "auth_user"."last_name",
       "auth_user"."email",
       "auth_user"."is_staff",
       "auth_user"."is_active",
       "auth_user"."date_joined"
FROM "auth_user"
WHERE ("auth_user"."first_name"::text LIKE R%
       AND NOT ("auth_user"."last_name"::text LIKE Z%))

  


student = Student.objects.all()  
for stu in student:  
    stu.fees *= 1.2  


from django.db.models import F  
  
Student.objects.update(fees=F('fees') * 1.2)




student = Student.objects.get(pk=1)  
student.price = F('fees') * 1.2  
student.save()  




 
select * from reseller_app_product;

-- agregate functin


from django.db.models import Avg
Book.objects.aggregate(Avg('price'))



>>> from django.db.models import Max
>>> Book.objects.aggregate(Max('price'))
{'price__max': Decimal('81.20')}


obj=Product.objects.all().a('p_price')
SELECT AVG(p_price) AS AvgMarks FROM reseller_app_product;


obj=Product.objects.all().count('p_price')
SELECT COUNT(p_price) FROM reseller_app_product;


SELECT FIRST(p_name) FROM reseller_app_product;


-- scalar function

SELECT  p_name ( UPPER (first_name) ) as product_name FROM reseller_app_product;

SELECT    UPPER (p_name) as product_name FROM reseller_app_product;
SELECT    LOWER(p_name) as product_name FROM reseller_app_product;