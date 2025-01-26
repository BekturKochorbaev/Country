
FROM node:18-alpine AS builder

WORKDIR /app

COPY package*.json ./
COPY next.config.ts ./

RUN npm install
RUN npm install @svgr/webpack

COPY . .

RUN npm run build

FROM node:18-alpine AS runner

WORKDIR /app

COPY --from=builder /app/next.config.js ./
COPY --from=builder /app/public ./public
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./package.json

EXPOSE 3000

CMD ["npm", "start"]
