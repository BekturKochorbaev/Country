/** @type {import('next').NextConfig} */
const path = require('path');

const nextConfig = {
  webpack(config) {
    config.module.rules.push({
      test: /\.svg$/,
      use: ["@svgr/webpack"]
    });

    config.resolve.alias['@'] = path.resolve(__dirname, 'src');
    config.resolve.alias['@/assets'] = path.resolve(__dirname, 'src/assets');

    return config;
  }
};

module.exports = nextConfig;
