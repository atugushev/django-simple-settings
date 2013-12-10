from django.shortcuts import render


def test_context_processor(request):
    return render(request, 'tests/test_template.html')
