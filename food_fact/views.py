from food_fact.models import Product, Nutrient
from django.core.paginator import Paginator
from food_fact import iteravel
from django.db.models import Q
from django.http import JsonResponse


def msg(request):
    """ 
        Essa função retorna um json com 2 elementos.
        1º Elemento: status code 200
        2º Elemento: mensagem "API Food Fact"
    """
    data = {
            'status_code': 200,
            'message': 'API Food Fact'
            }

    return return_data(data)


def list_products(request):
    """ 
        Essa função retorna um arquivo json com dois elementos.
        1º Elemento: O número de página do conteudo da response e a página atual
        2º Elemento: Uma lista com 10 elemento da página atual
       
    """
    products = Product.objects.all().order_by('id')
    if products:
        paginator = Paginator(products, 10)
        current_page = request.GET.get("page")
        page_obj = paginator.get_page(current_page)
        quantity_page = paginator.num_pages
        data = iteravel.products_iterables(page_obj, current_page, quantity_page)
    else:
        data = {
                'status_code': 204,
                'message': 'Sem conteúdo'
                }
    return return_data(data)


def get_product(request, code_product):

    """ 
        Essa view busca o id de um objeto na basse de dados. Se o id da requisição corresponde ao id de um objeto existente na base, a função retorna os dados do objeto no formato json.
        
        No entanto, se o objeto não existe na base, a função retornará um json com status code 204 e uma mensagem "Product not found".
    """
    try:
        product = Product.objects.get(code=code_product)
        data = iteravel.product_iterable(product)
    except:
        data = {
                'status_code': 404,
                'message': 'Product not found'
                }
    return return_data(data)

def search(request):

    search_value = request.GET.get('q', '').strip()

    products = Product.objects.\
            filter(
                Q(product_name__icontains=search_value) |
                Q(brands__icontains=search_value)
                ).\
            order_by('id')
    
    if search_value == '' or not products:
        data = {
                'status_code': 404,
                'message': 'Page not found'
                }
    else:
        paginator = Paginator(products, 10) # Show 10 contacts per page.
        current_page = request.GET.get("page")
        page_obj = paginator.get_page(current_page)
        quantity_page = paginator.num_pages
        data = iteravel.products_iterables(page_obj, current_page, quantity_page, search_value)
    
    return return_data(data)
    
def return_data(data):
    """
        Essa é uma views terciária.
        Ela é chamada em cada view pricipal, recebe o objeto tratado em cada view e o retorna no formato json.
    """
    return JsonResponse(
        data, safe=False, 
        json_dumps_params={
            'indent':4, 'ensure_ascii':False
            }
        )