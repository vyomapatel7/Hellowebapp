from django.shortcuts import render
# Create your views here.

def index(request):
    # defining the variable
    number = 6
    # don't forget the quotes because it's a string, not an integer
    thing = "Thing name"
    return render(request, 'index.html', {
        'number': number,
        # don't forget to pass it in, and the last comma
        'thing': thing,
})
