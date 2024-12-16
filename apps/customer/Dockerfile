# Apps Dockerfile (Expo)
FROM node:20-slim

# Install Expo CLI globally
RUN npm install -g expo-cli

# Set the working directory
WORKDIR /apps

# Copy the apps directory
COPY customer/ ./

# Install dependencies for all Expo apps
RUN npm install

# Expose the default Expo development server port
EXPOSE 8081

# Start Expo app
CMD ["expo", "start", "--tunnel"]
