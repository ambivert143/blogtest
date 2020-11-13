from django.shortcuts import render, redirect
from django.http import HttpResponse

posts = [
	{
		'tacgia': 'Nguồn instagram',
		'tieude': 'Blog 1',
		'noidung': 'Công thức 3 6 5',
		'date_posted': 'Tháng 11 Ngày 13 Năm 2020',
	},
	{
		'tacgia': 'Nguồn facebook',
		'tieude': 'Blog 2',
		'noidung': 'Công thức 21 3 6 5',
		'date_posted': 'Tháng 11 Ngày 13 Năm 2020',
	},
]

def home(request):
	context = {
		'posts': posts,
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title':'About'})
