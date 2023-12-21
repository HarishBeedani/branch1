FROM nginx:1.21-alpine
COPY . /usr/share/nginx/sample
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
