
FROM centos:7
RUN yum install -y python36-pip python36-setuptools python36 epel-release python36-devel httpd \
&& yum groupinstall -y "Development tools"
RUN easy_install-3.6 pip==19.3.1
RUN pip3 install keras==2.6.0
RUN pip3 install numpy pandas pillow opencv-python secure-smtplib 
RUN pip3 install tensorflow --no-cache-dir
CMD ["/usr/sbin/httpd","-D","FOREGROUND"]
