FROM node:23-slim

WORKDIR /app

COPY package*.json ./
COPY package-lock.json ./

# Clean install dependencies (skip native platform bindings)

RUN npm install --omit=optional
RUN npm install --platform=linux/arm64 --save-dev @vitejs/plugin-react
COPY . .


EXPOSE 5173
CMD ["npm", "run", "dev", "--", "--host"]
