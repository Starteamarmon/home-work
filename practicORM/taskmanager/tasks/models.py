from django.db import models, AbstractUser


class Project(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
      return self.name


class User(AbstractUser):
  firstname = models.CharField(max_length=100)
  lastname = models.CharField(max_length=100)

  def __str__(self):
    return self.username


class TaskStatus(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()

  def __str__(self):
    return self.name


class Task(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField()
  status = models.ForeignKey(TaskStatus, on_delete=models.DO_NOTHING)
  created_at = models.DateTimeField(auto_now_add=True)
  due_date = models.DateField()
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  performers = models.ManyToManyField(User)
  
  def __str__(self):
      return f'{self.title} ({self.status})'
  


