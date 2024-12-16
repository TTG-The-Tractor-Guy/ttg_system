# Admin Dockerfile (React)
FROM node:20-slim

# Set the working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY admin/package.json admin/package-lock.json* ./
RUN npm install

# Copy the React app code
COPY admin/ ./

# Build the React app
RUN npm run build

# Expose port
EXPOSE 3000

# Serve the build using a lightweight HTTP server
CMD ["npx", "serve", "-s", "build", "-l", "3000"]
