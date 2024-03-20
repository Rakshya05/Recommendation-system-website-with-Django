from django.db.models import Q
from django.shortcuts import render, redirect
from productApp.models import Products, Organization


# Create your views here.
def create_products(request):
    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        category = data.get('category')
        description = data.get('description')
        image = request.FILES.get('image')
        user = request.user if request.user.is_authenticated else None

        # Extract the selected keyword from the form data
        selected_keyword = data.get('keywords')
        selected_keywords_list = selected_keyword.split(',')

        print(selected_keywords_list)
        # Create the product and save it to the database
        Products.objects.create(
            user_id=user.id,
            category=category,
            description=description,
            name=name,
            image=image,
            keywords=selected_keywords_list
        )


    return render(request, 'donor.html')



def update_product(request, id):
    queryset = Products.objects.get(id=id)

    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        category = data.get('category')
        description = data.get('description')
        keywords = data.get('keywords')
        image = request.FILES.get('image')
        queryset.name = name
        queryset.category = category
        queryset.description = description
        queryset.keywords = keywords
        queryset.image = image
        print(data)
        queryset.save()
        return redirect('/')

    context = {'product': queryset, 'user': request.user}
    print(queryset.description)
    return render(request, 'update_product.html', context=context)


def get_product_details(request, product_id):
    user_id=request.user.id
    current_product = Products.objects.get(id=product_id)
    if Organization.objects.filter(user_id=user_id).exists():
        organization = Organization.objects.get(user_id=user_id)
        print(organization)
        products = Products.objects.all()

        similarities = calculate_similarity(organization, products)
        print(similarities)
        # Assuming products is a QuerySet and similarities is a list of similarity scores
        sorted_products = sort_products_by_similarity(products, similarities)
        top_4_products = sorted_products[:4]

        print(sorted_products)
        similarities = calculate_similarity(organization, sorted_products)
        print(similarities)
        context = {'product': current_product, 'products': top_4_products}
    else:
        print("not existed")
        context = {'product': current_product, 'products': False}
    # If organization with user_id doesn't exist, return the product details without similarities
    return render(request, 'product.html', context)



'''def get_product_details(request, product_id):
    current_product = Products.objects.get(id=product_id)
    if Organization.objects.filter(user_id=user_id).exists():
        organization = Organization.objects.get(user_id=user_id)
        products = Products.objects.all()

        similarities = calculate_similarity(organization, products)
        print(similarities)
        # Assuming products is a QuerySet and similarities is a list of similarity scores
        sorted_products = sort_products_by_similarity(products, similarities)
        top_4_products = sorted_products[:4]

        print(sorted_products)
        similarities = calculate_similarity(organization, sorted_products)
        print(similarities)
        context = {'product': current_product, 'products':top_4_products }



    # If organization with user_id doesn't exist, return the product details without similarities
    context = {'product': current_product,'products':False }
    return render(request, 'product.html', context)'''

def sort_products_by_similarity(products, similarities):
    # Combine products and similarities into a list of tuples
    product_similarity_pairs = list(zip(products, similarities))

    # Sort the list of tuples based on similarity (second element in the tuple)
    sorted_pairs = sorted(product_similarity_pairs, key=lambda x: x[1], reverse=True)

    # Extract sorted products from the sorted list of tuples
    sorted_products = [pair[0] for pair in sorted_pairs]

    return sorted_products




# Assuming products and similarities are already defined


'''current_keywords = current_product.keywords.split(', ')

    all_destinations = Products.objects.exclude(id=product_id)

    similar_destinations = []
    for i, sim_destination in enumerate(all_destinations):
        similar_keywords = sim_destination.keywords.split(', ')
        sim_score = get_cosine_similarity(current_keywords, similar_keywords)
        print(sim_score)
        similar_destinations.append({'destination': sim_destination, 'similarity': sim_score})
    print(similar_destinations)
    # Sort destinations by similarity in descending order
    similar_destinations = sorted(similar_destinations, key=lambda x: x['similarity'], reverse=True)
    print(similar_destinations)
    destination_objects = [item['destination'] for item in similar_destinations[:4]]
    print(destination_objects)'''



def CreateOrganization(request):
    if  request.user.id:
        user_id = request.user.id
        organizations = Organization.objects.filter(user_id=user_id)
        print("checking")
        print(len(organizations))
        print(request.user.id)


        if  organizations:
            print("already existed")
            return render(request, 'already.html')
        else:
            print("not already")
            if request.method == "POST":
        # Retrieve data from POST request
                name = request.POST.get('name')
                email = request.POST.get('email')
                phone = request.POST.get('phone')
                address = request.POST.get('address')
                website = request.POST.get('website')
                document_upload = request.FILES.get('documentUpload')
                description = request.POST.get('description')
                user_id = request.user.id

                keywords = request.POST.getlist('keywords')
                print(name)
                print(keywords)

                Organization.objects.create(
                    name=name,
                    email=email,
                    phone=phone,
                    address=address,
                    website=website,
                    document_upload=document_upload,
                    description=description,
                    user_id=user_id,
                    keywords=keywords
                )
                return render(request,'success.html')

        # Add checked keywords to the organization
    # Render the form template
            return render(request, 'organization.html')
    else:
        return render(request, 'login.html')


def products(request):
    queryset = Products.objects.all()

    # Sorting logic (default sorting order)
    sorted = quicksort(queryset)
    sorted_queryset = sorted[:8]

    user = request.user if request.user.is_authenticated else None

    if request.GET.get('search'):
        search_term = request.GET.get('search')
        search_terms = search_term.split()

        # Create a Q object for searching in the category
        category_query = Q()
        for term in search_terms:
            category_query |= Q(category__icontains=term)

        # Create a Q object for searching in the description
        description_query = Q()
        for term in search_terms:
            description_query |= Q(description__icontains=term)

        # Combine the two Q objects with an OR operator
        queryset = queryset.filter(category_query | description_query)

        # Sort the filtered queryset
        sorted_queryset = quicksort(queryset)

        context = {'products': sorted_queryset, 'user': user, 'terms': search_term}
        return render(request, 'searchresult.html', context=context)

    context = {'products': sorted_queryset, 'user': user}
    return render(request, 'index1.html', context=context)

def quicksort(arr):
    if len(arr) <= 1:
        return arr  # Already sorted

    # Call the method to get the average rating
    pivot = arr[len(arr) // 2].created_date
    left = [x for x in arr if x.created_date > pivot]
    middle = [x for x in arr if x.created_date == pivot]
    right = [x for x in arr if x.created_date < pivot]

    return quicksort(left) + middle + quicksort(right)


'''def delete_products(request,id):
    queryset = Products.objects.get(id=id)
    print(queryset)
    queryset.delete()
    return redirect('product.html')'''
def delete_products(request, product_id):
    # Retrieve the product with the specified ID
    try:
        product = Products.objects.get(id=product_id)
    except Products.DoesNotExist:
        # Handle the case where the product does not exist
        # You might want to add appropriate error handling here
        return redirect('delete.html')

    # Delete the product
    product.delete()

    # Redirect to the desired URL after deletion
    # Replace 'product.html' with the appropriate URL name or path
    return redirect('delete.html')

'''def jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union if union != 0 else 0

def calculate_similarity(organization, products):
    organization_set = set(organization)
    max_match_count = 0
    max_similarity = 0
    similarities = []
    for product in products:
        product_set = set(product)
        match_count = len(organization_set.intersection(product_set))
        max_match_count = max(max_match_count, match_count)
        union_size = len(organization_set.union(product_set))
        similarity = jaccard_similarity(organization_set, product_set)
        similarities.append(similarity)
    return similarities'''


def jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union if union != 0 else 0


def calculate_similarity(organization, products):
    organization_set = set(organization.keywords)
    max_match_count = 0
    max_similarity = 0
    similarities = []

    for product in products:
        product_set = set(product.keywords)
        match_count = len(organization_set.intersection(product_set))
        max_match_count = max(max_match_count, match_count)

        union_size = len(organization_set.union(product_set))
        similarity = jaccard_similarity(organization_set, product_set)
        similarities.append(similarity)

    return similarities

