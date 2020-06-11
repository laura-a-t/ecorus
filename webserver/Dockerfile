FROM nginx:1.18

# Remove default nginx config
RUN rm -f /etc/nginx/conf.d/default.conf

# Copy own nginx conf
COPY nginx.conf /etc/nginx/conf.d