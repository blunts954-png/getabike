/** @type {import('next').NextConfig} */
const nextConfig = {
  // Output configuration for static export
  output: 'export',
  distDir: 'dist',
  
  // Image optimization settings
  images: {
    unoptimized: true,
  },
  
  // Compression
  compress: true,
  
  // Trailing slashes for SEO
  trailingSlash: true,
  
  // Performance optimizations
  poweredByHeader: false,
  generateEtags: true,
  
  // Turbopack config (empty to enable)
  turbopack: {},
  
  // Experimental features
  experimental: {
    optimizeCss: true,
    scrollRestoration: true,
  },
};

export default nextConfig;
