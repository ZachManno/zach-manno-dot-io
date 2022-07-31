FROM amazonlinux
RUN yum install httpd -y
RUN yum groupinstall "development tools" -y
RUN yum install -y wget

# Install rust
RUN amazon-linux-extras install rust1
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | bash -s -- -y
RUN source /root/.cargo/env
#RUN /root/.cargo/bin/rustup update stable
RUN /root/.cargo/bin/rustup install 1.57.0
RUN /root/.cargo/bin/rustup default 1.57.0
#RUN mkdir /rustinstall
#RUN export HOME="/rustinstall"
#RUN echo "HOME: $HOME"
#RUN export PATH="$HOME/.cargo/bin:$PATH" && echo "installed package. Path: $PATH"
#RUN echo "installed package. Path: $PATH"
#RUN rustup install 1.57.0

COPY . .
RUN export PKG_CONFIG_ALLOW_CROSS=1
RUN PKG_CONFIG_ALLOW_CROSS=1 /root/.cargo/bin/cargo build
#COPY index.html /var/www/html/

#CMD ["/usr/sbin/httpd","-D","FOREGROUND"]
