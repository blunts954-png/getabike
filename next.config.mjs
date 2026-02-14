import path from 'path';

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
  turbopack: {
    // Use an absolute project root to avoid ambiguous workspace detection on CI (Vercel).
    root: path.resolve('.'),
  },
  
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
