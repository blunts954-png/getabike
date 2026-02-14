import { Space_Grotesk, Cinzel, Bebas_Neue } from "next/font/google";
import "./globals.css";

const spaceGrotesk = Space_Grotesk({
  subsets: ["latin"],
  variable: "--font-space-grotesk",
  display: "swap",
  weight: ["300", "400", "500", "600", "700"],
});

const cinzel = Cinzel({
  subsets: ["latin"],
  variable: "--font-cinzel",
  display: "swap",
  weight: ["400", "500", "600", "700"],
});

const bebas = Bebas_Neue({
  subsets: ["latin"],
  variable: "--font-bebas",
  display: "swap",
  weight: ["400"],
});

// Enhanced metadata for maximum GEO/AEO performance
export const metadata = {
  metadataBase: new URL("https://getabike.com"),
  
  // Primary SEO
  title: {
    default: "Get A Bike Bakersfield | Luxury Certified Pre-Owned Bikes",
    template: "%s | Get A Bike Bakersfield",
  },
  description: "Bakersfield's premier certified pre-owned bicycle dealership. Premium road, gravel, mountain & electric bikes. Appointment-only concierge service. 90-day warranty. Trade-ins welcome.",
  keywords: [
    "luxury bikes Bakersfield",
    "certified pre-owned bicycles",
    "premium road bikes",
    "electric bikes Bakersfield",
    "bike shop near me",
    "bicycle dealership",
    "bike fitting Bakersfield",
    "high-end bikes",
    "performance bicycles",
    "bike trade-in Bakersfield",
    "gravel bikes",
    "mountain bikes",
    "carbon fiber bikes",
    "bicycle warranty",
    "luxury cycling",
  ],
  
  // Canonical
  alternates: {
    canonical: "/",
  },
  
  // Robots
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      "max-video-preview": -1,
      "max-image-preview": "large",
      "max-snippet": -1,
    },
  },
  
  // Open Graph
  openGraph: {
    title: "Get A Bike Bakersfield | Luxury Certified Pre-Owned Bikes",
    description: "Bakersfield's premier certified pre-owned bicycle dealership. Premium road, gravel, mountain & electric bikes with concierge service.",
    url: "https://getabike.com",
    siteName: "Get A Bike Bicycles",
    locale: "en_US",
    type: "website",
    images: [
      {
        url: "/og-image.jpg",
        width: 1200,
        height: 630,
        alt: "Get A Bike Bakersfield - Luxury Certified Pre-Owned Bicycles",
      },
    ],
  },
  
  // Twitter
  twitter: {
    card: "summary_large_image",
    title: "Get A Bike Bakersfield | Luxury Certified Pre-Owned Bikes",
    description: "Bakersfield's premier certified pre-owned bicycle dealership. Premium bikes, concierge service.",
    images: ["/og-image.jpg"],
    creator: "@getabikebakersfield",
  },
  
  // Verification
  verification: {
    google: "your-google-verification-code",
    yandex: "your-yandex-verification-code",
  },
  
  // Apple
  appleWebApp: {
    capable: true,
    title: "Get A Bike",
    statusBarStyle: "black-translucent",
  },
  
  // Icons
  icons: {
    icon: [
      { url: "/favicon.ico", sizes: "any" },
      { url: "/icon.svg", type: "image/svg+xml" },
    ],
    apple: [
      { url: "/apple-touch-icon.png", sizes: "180x180" },
    ],
    other: [
      {
        rel: "mask-icon",
        url: "/safari-pinned-tab.svg",
        color: "#c9a962",
      },
    ],
  },
  
  // Manifest
  manifest: "/manifest.json",
  
  // Other
  category: "business",
  classification: "Bicycle Store",
  authors: [{ name: "Get A Bike Bicycles" }],
  creator: "Get A Bike Bicycles",
  publisher: "Get A Bike Bicycles",
  formatDetection: {
    telephone: true,
    date: true,
    address: true,
    email: true,
    url: true,
  },
};

// Viewport configuration
export const viewport = {
  width: "device-width",
  initialScale: 1,
  maximumScale: 5,
  themeColor: [
    { media: "(prefers-color-scheme: light)", color: "#ffffff" },
    { media: "(prefers-color-scheme: dark)", color: "#050505" },
  ],
  colorScheme: "dark",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en" className="scroll-smooth">
      <head>
        {/* Preconnect to external domains */}
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
        
        {/* Geo Tags for Local SEO */}
        <meta name="geo.region" content="US-CA" />
        <meta name="geo.placename" content="Bakersfield" />
        <meta name="geo.position" content="35.3733;-119.0187" />
        <meta name="ICBM" content="35.3733, -119.0187" />
        
        {/* Local Business Meta */}
        <meta name="business:contact_data:street_address" content="213 E 18th St" />
        <meta name="business:contact_data:locality" content="Bakersfield" />
        <meta name="business:contact_data:region" content="CA" />
        <meta name="business:contact_data:postal_code" content="93305" />
        <meta name="business:contact_data:country_name" content="USA" />
        <meta name="business:contact_data:phone_number" content="+1-661-555-0100" />
        <meta name="business:contact_data:website" content="https://getabike.com" />
        
        {/* Open Graph Location */}
        <meta property="place:location:latitude" content="35.3733" />
        <meta property="place:location:longitude" content="-119.0187" />
        
        {/* Dublin Core */}
        <meta name="DC.title" content="Get A Bike Bakersfield" />
        <meta name="DC.identifier" content="https://getabike.com" />
        <meta name="DC.description" content="Bakersfield's premier certified pre-owned bicycle dealership" />
        <meta name="DC.subject" content="Bicycles, Cycling, Bike Shop" />
        <meta name="DC.language" content="en-US" />
        <meta name="DC.coverage" content="Bakersfield, CA" />
        
        {/* Mobile Web App */}
        <meta name="mobile-web-app-capable" content="yes" />
        <meta name="application-name" content="Get A Bike" />
        
        {/* Apple */}
        <meta name="apple-mobile-web-app-capable" content="yes" />
        <meta name="apple-mobile-web-app-title" content="Get A Bike" />
        <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
        
        {/* Microsoft */}
        <meta name="msapplication-TileColor" content="#050505" />
        <meta name="msapplication-TileImage" content="/mstile-144x144.png" />
        <meta name="msapplication-config" content="/browserconfig.xml" />
        
        {/* Theme */}
        <meta name="theme-color" content="#050505" />
        <meta name="msapplication-navbutton-color" content="#050505" />
      </head>
      <body
        className={`${spaceGrotesk.variable} ${cinzel.variable} ${bebas.variable} antialiased`}
      >
        {children}
      </body>
    </html>
  );
}
