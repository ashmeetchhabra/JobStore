import webapp2
from webapp2_extras import sessions
from google.appengine.ext import ndb
import time
import datetime
# student_user_name='null'
head='''
<head>
<script src= "http://ajax.googleapis.com/ajax/libs/angularjs/1.3.14/angular.min.js"></script>  
<center><h1><p style="color:#6699FF">Welcome to the Jobstore</p></h1></center></head>
<body bgcolor="#E6E6FA">
'''
select="""
<center>
Looking for a dream job or a reliable employee?<br>
You are a:
    
               
<table>
<form action="/student" method="post">
      <tr><input type="submit" value="student"> or
      </form>
<form action="/recruiter" method="post">
     <tr><input type="submit" value="recruiter"></tr>
    </form>           
</table>
        

 
</center>
"""

LoginForm_stu="""
<center>
<form action="/login_stu" method="post">
Login Form for Students:
      <table>
      <tr><td>username:</td><td><input type='text' name="username_stu"></td></tr>
      <tr><td>password:</td><td><input type='password' name="password_stu" ></td></tr>
      <tr><td><input type="submit" value="Submit"><input type="reset" value="Reset">

    </form>
<form action="/register_stu" method="post">
<input type="submit" value="Register"></td></tr>
</form>
   </table>
        

 
</center>
"""
LoginForm_rec="""
<center>
<form action="/login_rec" method="post">
Login Form for Recruiter:
      <table>
      <tr><td>username:</td><td><input type='text' name="username_rec"></td></tr>
      <tr><td>password:</td><td><input type='password' name="password_rec" ></td></tr>
      <tr><td><input type="submit" value="Submit"><input type="reset" value="Reset">

    </form>
<form action="/register_rec" method="post">
<input type="submit" value="Register"></td></tr>
</form>
   </table>
        

 
</center>
"""

SignupForm_stu="""
<center>
<form action="/signup_stu" method="post" >
Add Details for Students:
      <table>
      <tr><td>First Name:</td><td><input type='text' name="firstname_stu" ></td></tr>
      <tr><td>Last Name:</td><td><input type='text' name="lastname_stu"></td></tr>
      <tr><td>Salary:</td><td><input type='text' name="salary_stu"></td></tr>
      <tr><td>Skills:</td><td><input type='text' name="skills_stu"></td></tr>
      <tr><td>Location:</td><td><input type='text' name="location_stu"></td></tr>
      <tr><td>Experience:</td><td><input type='text' name="exp_stu"></td></tr>
      <tr><td>Email id:</td><td><input type='text' name="email_stu"></td></tr>
      <tr><td>User Name:</td><td><input type='text' name="username_stu"></td></tr>
      <tr><td>Password:</td><td><input type='password' name="password_stu" ></td></tr>
      <tr><td></td><td><input type="submit" value="Submit"><input type="reset" value="Reset">
    </form></center>
"""

SignupForm_rec="""
<center>
<form action="/signup_rec" method="post" >
Add Details for Job:
      <table>
      <tr><td>Company Name:</td><td><input type='text' name="companyname_rec" ></td></tr>
      <tr><td>Salary Provided:</td><td><input type='text' name="salary_rec"></td></tr>
      <tr><td>Skills Needed:</td><td><input type='text' name="skills_rec"></td></tr>
      <tr><td>Location:</td><td><input type='text' name="location_rec"></td></tr>
      <tr><td>Link to apply:</td><td><input type='text' name="link_rec"></td></tr>
      <tr><td>Experience:</td><td><input type='text' name="exp_rec"></td></tr>
      <tr><td>User Name:</td><td><input type='text' name="username_rec"></td></tr>
      <tr><td>Password:</td><td><input type='password' name="password_rec" ></td></tr>
      <tr><td></td><td><input type="submit" value="Submit"><input type="reset" value="Reset">
    </form></center>
"""

class LoginDB_stu(ndb.Model):
    first_name=ndb.StringProperty()
    last_name=ndb.StringProperty()
    stu_salary=ndb.StringProperty()
    stu_skills=ndb.StringProperty()
    stu_location=ndb.StringProperty()
    stu_exp=ndb.StringProperty()
    stu_email=ndb.StringProperty()
    stu_password=ndb.StringProperty()
    stu_username=ndb.StringProperty()


class LoginDB_rec(ndb.Model):
    company_name=ndb.StringProperty()
    # last_name=ndb.StringProperty()
    rec_salary=ndb.StringProperty()
    rec_skills=ndb.StringProperty()
    rec_location=ndb.StringProperty()
    rec_link=ndb.StringProperty()
    rec_exp=ndb.StringProperty()
    rec_password=ndb.StringProperty()
    rec_username=ndb.StringProperty()


class MainStu(webapp2.RequestHandler):
    def post(self):
        self.response.write('<html>'+head+'<body>'+LoginForm_stu+'</body></html>')

class MainRec(webapp2.RequestHandler):
    def post(self):
        self.response.write('<html>'+head+'<body>'+LoginForm_rec+'</body></html>')        

class LoginHandler_stu(webapp2.RequestHandler):
    c=100
    def post(self):
        global student_user_name
        global student_password
        #self.response.write("list of companies")  
        
        student_user_name=self.request.get('username_stu')
        student_password=self.request.get('password_stu')

        q=LoginDB_stu.query(LoginDB_stu.stu_username==student_user_name)
        self.response.write('<br>')
        self.response.write('<br>')
        
        x=q.fetch()
        if len(x)==0:
            self.response.write(head+'please sign up')
        else:
            for i in x:
                
                #z=dict(x)
                #print (json.dumps({x}))
                pwd_stu=i.stu_password
                fn_stu=i.first_name
                ln_stu=i.last_name
                sal_stu=i.stu_salary
                skill_stu=i.stu_skills
                loc_stu=i.stu_location
                exp_stu=i.stu_exp
                email_stu=i.stu_email
                LoginHandler_stu.c=200
                
                #print (json.dumps(pwd_stu))
                #self.response.write(json.dumps(fn_stu))
                #self.response.write(json.dumps(pwd_stu))

                
                # self.response.write(' ')
                # self.response.write('<br>')



                # q1=ndb.gql("Select * from LoginDB_rec")
                # for h in q1:
                #   com_name=h.company_name
                #   com_location=h.rec_location
                #   # com_pwd=h.rec_password
                #   com_sal=h.rec_salary
                #   com_skills=h.rec_skills
                #   com_link=h.rec_link

                #   # self.response.write(h)

                #   self.response.write('<br>')
                #   self.response.write('<br>')

                #   self.response.write('<br><html><body><b>Company Profile:</b><br>Company name is: '+com_name+'<br>Location:'+com_location+'<br>salary: '+com_sal+
                # '<br>skills needed are:'+com_skills+'<br><a href="'+com_link+'">Apply</a>')




            if pwd_stu==student_password:
                self.response.write('<br><html><body><b>Your Profile:</b><br>your name is: '+fn_stu+' '+ln_stu+'<br>salary needed is: '+sal_stu+
                '<br>skills are:'+skill_stu+'<br>locations is: '+loc_stu+'<br>'+'experience is'+exp_stu+'<br>'+'Email is '+email_stu+'<br>')

                
                self.response.write('''<form action="/search_stu" method="post">
                                        <input type='text' name="search_skills" placeholder="Skills">
                                        <input type='text' name="search_sal" placeholder="Salary"><br>
                                        <input type='text' name="search_loc" placeholder="Location">
                                        <input type='text' name="search_exp" placeholder="Experience">
                                        <input type="submit" value="Search">
                                        </form><br>
                                        <form action ="/update_stu" method = "post">
                                        <input type="submit" value="Update Profile">
                                        </form>

                                    ''')




              # student_user_name=self.request.get('username_stu')
              # student_password=self.request.get('password_stu')
                # self.response.write('<br>')
                self.response.write('<br>')
                # self.response.write('<b>Company Profile:</b>')
                # q=LoginDB_stu.query(LoginDB_stu.stu_username==student_user_name)
                # x=q.fetch()
                # if len(x)==0:
                #     self.response.write(head+'please sign up')
                # else:
                #     for i in x:

                #         q1=ndb.gql("Select * from LoginDB_rec")
                #         for h in q1:
                #             com_name=h.company_name
                #             com_location=h.rec_location
                #             # com_pwd=h.rec_password
                #             com_sal=h.rec_salary
                #             com_skills=h.rec_skills
                #             com_link=h.rec_link

                #             # self.response.write(h)

                #             # self.response.write('<br>')
                            

                #             self.response.write('<br><html><body><br><b>'+com_name+'</b><br>Location:'+com_location+'<br>salary: '+com_sal+
                #             '<br>skills needed are:'+com_skills+'<br><a href="'+com_link+'">Apply</a>')
                # return abc
            else:
                self.response.write('password does not match')

    # def disp(self):
    #     # self.response.write('the value of c is')
    #     print("the username is ", LoginHandler_stu.un)
    #     return LoginHandler_stu.un
        # self.response.write(LoginHandler_stu.c)
        # print('the value of c is:',LoginHandler_stu.c)
    



class SearchHandler_stu(webapp2.RequestHandler):
    def post(self):
      self.response.write('<b>Company Profile:</b>')
                # q=LoginDB_stu.query(LoginDB_stu.stu_username==student_user_name)
                # x=q.fetch()
                # if len(x)==0:
                    
                # else:
                    # for i in x:

      key_skill=self.request.get('search_skills')
      key_sal=self.request.get('search_sal')
      key_loc=self.request.get('search_loc')
      key_exp=self.request.get('search_exp')

      # if key_skill=="":
      #     self.response.write("skill is None<br>")
      # else:
      #     self.response.write("skill is "+key_skill+"<br>")
      #     self.response.write("Key is "+key_skill+"<br>")

      # if key_sal=="":
      #     self.response.write("sal is None<br>")
      # else:
      #     self.response.write("salary is "+key_sal+"<br>")

      # if key_loc=="":
      #     self.response.write("loc is None<br>")
      # else:
      #     self.response.write("location is "+key_loc+"<br>")

      # if key_exp=="":
      #     self.response.write("exp is None<br>")
      # else:
      #     self.response.write("exp is "+key_exp+"<br>")

      if key_skill==key_sal==key_exp==key_loc=="":
          self.response.write("Give atleast one entry<br>")
      else:
      

          # self.response.write("Key is "+key_skill)

          q1=ndb.gql("Select * from LoginDB_rec")
          # y=q1.fetch()
          # if len(y)==0:
          #     self.response.write(head+'No Records')
          # else:
          for h in q1:
          
              com_name=h.company_name
              com_location=h.rec_location
              # com_pwd=h.rec_password
              com_sal=h.rec_salary
              com_skills=h.rec_skills
              com_link=h.rec_link
              com_exp=h.rec_exp
              f=0
              # self.response.write(h)
              if key_skill==com_skills and f<>1:
                  self.response.write('<br><html><body><br><b>'+com_name+'</b><br>Location:'+com_location+'<br>salary: '+com_sal+
                  '<br>skills needed are:'+com_skills+'<br><a href="'+com_link+'">Apply</a><br>'+'Experience:'+com_exp)
                  f=1

              if key_sal==com_sal and f<>1:
                  self.response.write('<br><html><body><br><b>'+com_name+'</b><br>Location:'+com_location+'<br>salary: '+com_sal+
                  '<br>skills needed are:'+com_skills+'<br><a href="'+com_link+'">Apply</a><br>'+'Experience:'+com_exp)
                  f=1

              if key_loc==com_location and f<>1:
                  self.response.write('<br><html><body><br><b>'+com_name+'</b><br>Location:'+com_location+'<br>salary: '+com_sal+
                  '<br>skills needed are:'+com_skills+'<br><a href="'+com_link+'">Apply</a><br>'+'Experience:'+com_exp)
                  f=1

              if key_exp==com_exp and f<>1:
                  self.response.write('<br><html><body><br><b>'+com_name+'</b><br>Location:'+com_location+'<br>salary: '+com_sal+
                  '<br>skills needed are:'+com_skills+'<br><a href="'+com_link+'">Apply</a><br>'+'Experience:'+com_exp)
                  f=1


              # else:
              #     self.response.write(head+'No Records')

              # self.response.write(h)
              # self.response.write('<br>')
              

              # self.response.write('<br><html><body><br><b>'+com_name+'</b><br>Location:'+com_location+'<br>salary: '+com_sal+
              # '<br>skills needed are:'+com_skills+'<br><a href="'+com_link+'">Apply</a>')


class UpdateHandler_stu(LoginHandler_stu):

    
    def post(self):
      self.response.write("update")
      # obj=LoginHandler_stu()
      # obj.post()
      # update_username=obj.disp()
      # print("update calling username",update_username)
      # self.response.write('update calling username')
      # self.response.write(update_username)


      # obj=LoginHandler_stu(webapp2)
      # xyz=obj.post()

      # p=LoginDB_stu.query(LoginDB_stu.stu_username==student_user_name)
      # a=p.fetch()
      # self.response.write(a)      

      self.response.write("""
        <center>
        <form action="/updated_stu" method="post" >
        Update Details for Students:
        <table>
        <tr><td>First Name:</td><td><input type='text' name="firstname_stu" ></td></tr>
        <tr><td>Last Name:</td><td><input type='text' name="lastname_stu"></td></tr>
        <tr><td>Salary:</td><td><input type='text' name="salary_stu"></td></tr>
        <tr><td>Skills:</td><td><input type='text' name="skills_stu"></td></tr>
        <tr><td>Location:</td><td><input type='text' name="location_stu"></td></tr>
        <tr><td>Experience:</td><td><input type='text' name="exp_stu"></td></tr>
        <tr><td>Email id:</td><td><input type='text' name="email_stu"></td></tr>
        <tr><td>User Name:</td><td><input type='text' name="username_stu"></td></tr>
        <tr><td>Password:</td><td><input type='password' name="password_stu" ></td></tr>
        <tr><td></td><td><input type="submit" value="Submit"><input type="reset" value="Reset">
        </form></center>
        """)
        
      # obj=LoginHandler_stu()
      # test=obj.disp()
      # self.response.write(test)

class LoginHandler_rec(webapp2.RequestHandler):
    def post(self):
        global company_user_name
        global company_password
        #self.response.write("list of companies")  
        
        company_user_name=self.request.get('username_rec')
        company_password=self.request.get('password_rec')

        r=LoginDB_rec.query(LoginDB_rec.rec_username==company_user_name)
        self.response.write('<br>')
        self.response.write('<br>')
        
        y=r.fetch()
        if len(y)==0:
            self.response.write(head+'please sign up')
        else:
            for i in y:
                
                #z=dict(x)
                #print (json.dumps({x}))
                pwd_rec=i.rec_password
                c_name=i.company_name
                #ln_stu=i.last_name
                sal_rec=i.rec_salary
                skill_rec=i.rec_skills
                loc_rec=i.rec_location
                
                #print (json.dumps(pwd_stu))
                #self.response.write(json.dumps(fn_stu))
                #self.response.write(json.dumps(pwd_stu))

                
                self.response.write(' ')
                self.response.write('<br>')



            if pwd_rec==company_password:
                self.response.write('<br><html><body>Company name is: '+c_name+'<br>Salary to be given is: '+sal_rec+
                '<br>skills needed are:'+skill_rec+'<br>locations is: '+loc_rec)
                self.response.write('</body></html>')
                
            else:
                self.response.write('password does not match')


class RegistrationForm_stu(webapp2.RequestHandler):
    def post(self):
        self.response.write('<html><body>'+SignupForm_stu+'</body></html>')

class RegistrationForm_rec(webapp2.RequestHandler):
    def post(self):
        self.response.write('<html><body>'+SignupForm_rec+'</body></html>')
     
class SignupHandler_stu(webapp2.RequestHandler):
    def post(self):
        login_details_stu=LoginDB_stu(first_name=self.request.get('firstname_stu'),
                                      last_name=self.request.get('lastname_stu'),
                                      stu_salary=self.request.get('salary_stu'),
                                      stu_skills=self.request.get('skills_stu'),
                                      stu_location=self.request.get('location_stu'),
                                      stu_exp=self.request.get('exp_stu'),
                                      stu_email=self.request.get('email_stu'),
                                      stu_password=self.request.get('password_stu'),
                                      stu_username=self.request.get('username_stu'))
                                      #apply_date =datetime.datetime.now().strftime("%d-%m-%y"))
                           
        login_details_stu.put()
        self.response.write('database updated')

class SignupHandler_rec(webapp2.RequestHandler):
    def post(self):
        login_details_rec=LoginDB_rec(company_name=self.request.get('companyname_rec'),
                                      #last_name=self.request.get('lastname_stu'),
                                      rec_salary=self.request.get('salary_rec'),
                                      rec_skills=self.request.get('skills_rec'),
                                      rec_location=self.request.get('location_rec'),
                                      rec_exp=self.request.get('exp_rec'),
                                      rec_password=self.request.get('password_rec'),
                                      rec_username=self.request.get('username_rec'),
                                      rec_link=self.request.get('link_rec'))
                                      #apply_date =datetime.datetime.now().strftime("%d-%m-%y"))
                           
        login_details_rec.put()
        self.response.write('database updated')



class Welcome(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('<html>'+head+'<body>'+select+'</body></html>')

app = webapp2.WSGIApplication([
    ('/', Welcome),('/student',MainStu),('/login_stu',LoginHandler_stu),('/register_stu',RegistrationForm_stu),('/signup_stu',SignupHandler_stu),('/recruiter',MainRec),('/login_rec',LoginHandler_rec),('/register_rec',RegistrationForm_rec),('/signup_rec',SignupHandler_rec),('/search_stu',SearchHandler_stu),('/update_stu',UpdateHandler_stu)], debug=True)

