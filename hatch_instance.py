# creates an ec2 instance, a t2.micro in us-west-2 with vockey.
# prints a message when the instance has been created

from ec2_setup import create_instance

create_instance("ami-08e2d37b6a0129927","t2.micro","vockey")
print("Congrats! It's a genderfluid virtual robot!")
