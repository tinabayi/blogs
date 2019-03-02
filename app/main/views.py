from flask import render_template,request,redirect,url_for,abort
 
from . import main
from .forms import BlogForm,UpdateProfile
# from .. import db

from .forms import BlogForm

from flask_login import login_required 

from flask import render_template,redirect,url_for, abort
from . import main

from .. import db,photos
from ..models import User,Blog,Comment,Subscribe
from .forms import BlogForm,CommentForm


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    all_blogs = Blog.get_blogs()
    
    title = 'Home - Welcome to The best pitches Website Online'

    return render_template('index.html', title = title ,all_blogs = all_blogs)


@main.route('/blog/new', methods = ['GET','POST'])
def new_blog():
    form = BlogForm()
    blogs =Blog.get_blogs()

    if form.validate_on_submit():
       
        description = form.description.data
        new_blog = Blog(description=description)
        new_blog.save_blogs()
        return redirect(url_for('main.index',description=description))
        

    title = 'Welcome to The best blogs Website Online'
    return render_template('blog.html',title = title, Blog_form=form,blogs=blogs)


@main.route('/blogs')
def dipslay_blogs():
   all_blogs = Blog.blogs()
   print(all_blogs)
   return render_template("index.html",all_blogs=all_blogs) 

@main.route('/blog/new', methods = ['GET','POST'])
@login_required
def create_blog():
   form = BlogForm()
   Blog = blog.Blog


   if form.validate_on_submit():
       # title = form.title.data
       teaser = form.teaser.data
       blog = form.blog.data
       new_blog = Blog(user_id=current_user.id,teaser=teaser, blog=blog)
       new_blog.save_new()
       return redirect(url_for('.index',blog = blog))

   # username = f'{user.username} pitch'
   return render_template('blog.html', blog_form=form)


@main.route('/blogs')
def display_blog():
   all_blogs = Blog.get_blogs()
   print(all_blogs)
   return render_template("index.html",all_blogs=all_blogs)


@main.route('/comment/new/<int:id>', methods = ['GET','POST'])
def new_comment(id):
    form = CommentForm()
    # comments =Comment.get_comments()

    if form.validate_on_submit():
       
        comment = form.comment.data
        new_comment = Comment(comment=comment)
        new_comment.save_comments()
        return redirect(url_for('main.index'))
    
    comments=Comment.query.filter_by(blog_id=id).all()

    title = 'Welcome to The best blogs Website Online'
    return render_template('comment.html',comments=comments,Comment_form=form)


@main.route('/comments')
def dipslay_comments():
  
   all_comments = Comment. get_comments()
   print(all_comments)
   return render_template("index.html",all_comments=all_comments) 





# @main.route('/user/<uname>/update/pic',methods= ['POST'])
# @login_required
# def update_pic(uname):
#     user = User.query.filter_by(username = uname).first()
#     if 'photo' in request.files:
#         filename = photos.save(request.files['photo'])
#         path = f'photos/{filename}'
#         user.profile_pic_path = path
#         db.session.commit()
#         return redirect(url_for('main.profile',uname=uname)
#         return render_template("profile/profile.html", user = user)

# @main.route('/user/<uname>')
# def profile(uname):
#     user = User.query.filter_by(username = uname).first()

#     if user is None:
#         abort(404)

#     return render_template("profile/profile.html", user = user)



# @main.route('/user/<uname>/update',methods = ['GET','POST'])
# @login_required
# def update_profile(uname):
#     user = User.query.filter_by(username = uname).first()
#     if user is None:
#         abort(404)

#     form = UpdateProfile()

#     if form.validate_on_submit():
#         user.bio = form.bio.data

#         db.session.add(user)
#         db.session.commit()

#         return redirect(url_for('.profile',uname=user.username))

#     return render_template('profile/update.html',form =form) 
