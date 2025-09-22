# Stage 1: Build Angular app
FROM node:20-alpine AS build

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

RUN npm run build --prod

# Stage 2: Serve with Nginx
FROM nginx:alpine

# Copy Angular build output
COPY --from=build /app/dist/frontend/browser /usr/share/nginx/html

# Copy nginx.conf
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
