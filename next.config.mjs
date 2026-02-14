/** @type {import('next').NextConfig} */
const nextConfig = {
  // For Vercel deployment, we use standard server-side rendering
  // Static export is handled by Vercel automatically
  
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
  
  // Turbopack config
  turbopack: {},
  
  // Experimental features
  experimental: {
    optimizeCss: true,
    scrollRestoration: true,
  },
  
  // Redirects for SEO
  async redirects() {
    return [
      {
        source: '/home',
        destination: '/',
        permanent: true,
      },
    ];
  },
};

export default nextConfig;
