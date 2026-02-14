"use client";

import { useEffect, useRef, useState } from "react";

// Bike inventory data
const bikes = [
  {
    id: 1,
    name: "Trek Madone SLR 9",
    category: "Road",
    specs: "56cm | Shimano Dura-Ace Di2",
    price: "$6,499",
    originalPrice: "$12,500",
    image: "/assets/bike-1.jpg",
    badge: "Certified",
  },
  {
    id: 2,
    name: "Specialized S-Works Tarmac",
    category: "Road",
    specs: "54cm | SRAM Red eTap AXS",
    price: "$7,299",
    originalPrice: "$14,000",
    image: "/assets/bike-2.jpg",
    badge: "Like New",
  },
  {
    id: 3,
    name: "Cervélo R5 Disc",
    category: "Road",
    specs: "58cm | Ultegra Di2",
    price: "$4,899",
    originalPrice: "$9,500",
    image: "/assets/bike-3.jpg",
    badge: "Certified",
  },
  {
    id: 4,
    name: "3T Exploro Racemax",
    category: "Gravel",
    specs: "56cm | Eagle AXS",
    price: "$3,799",
    originalPrice: "$7,200",
    image: "/assets/bike-4.jpg",
    badge: "Rare Find",
  },
  {
    id: 5,
    name: "Specialized Turbo Levo",
    category: "Electric",
    specs: "M | 90mi Range | Carbon",
    price: "$8,999",
    originalPrice: "$15,000",
    image: "/assets/bike-1.jpg",
    badge: "Premium",
  },
  {
    id: 6,
    name: "Santa Cruz Hightower",
    category: "Mountain",
    specs: "L | XX1 AXS Reserve",
    price: "$5,499",
    originalPrice: "$10,500",
    image: "/assets/bike-2.jpg",
    badge: "Certified",
  },
  {
    id: 7,
    name: "Canyon Grail CF SLX",
    category: "Gravel",
    specs: "M | GRX Di2 | Carbon",
    price: "$3,299",
    originalPrice: "$6,500",
    image: "/assets/bike-3.jpg",
    badge: "Certified",
  },
  {
    id: 8,
    name: "BMC Roadmachine 01",
    category: "Endurance",
    specs: "54cm | Force AXS",
    price: "$4,199",
    originalPrice: "$8,500",
    image: "/assets/bike-4.jpg",
    badge: "Like New",
  },
];

// Testimonials data
const testimonials = [
  {
    id: 1,
    text: "The appointment-only experience was exceptional. No pressure, expert fitting, and they found me the perfect carbon road bike within my budget.",
    author: "Marcus Chen",
    title: "Triathlete",
    rating: 5,
    avatar: "/assets/avatar-1.jpg",
  },
  {
    id: 2,
    text: "Traded in my old bike and walked out with a like-new Specialized. The 90-day warranty gives total peace of mind. Best bike shop in Kern County.",
    author: "Sarah Williams",
    title: "Gran Fondo Rider",
    rating: 5,
    avatar: "/assets/avatar-2.jpg",
  },
  {
    id: 3,
    text: "As a serious cyclist, I appreciate their curated inventory. Every bike is genuinely certified, not just cleaned up. Worth every penny.",
    author: "David Rodriguez",
    title: "Cat 1 Racer",
    rating: 5,
    avatar: "/assets/avatar-3.jpg",
  },
];

// Events data
const events = [
  { name: "Hart Park Sunrise Ride", date: "Feb 22, 6:30 AM" },
  { name: "Kern River Trail Skills Workshop", date: "Mar 8, 9:00 AM" },
  { name: "Private Bike Fitting Session", date: "By Appointment" },
];

// Blog data
const blogPosts = [
  { category: "Buying Guide", title: "How to Choose a Certified Pre-Owned Carbon Road Bike" },
  { category: "Maintenance", title: "The Complete Guide to Di2 Electronic Shifting Care" },
  { category: "Local", title: "Top 10 Scenic Cycling Routes in Kern County" },
];

// Instagram images
const instagramImages = [
  "/assets/insta-1.jpg",
  "/assets/insta-2.jpg",
  "/assets/insta-3.jpg",
  "/assets/insta-4.jpg",
  "/assets/insta-5.jpg",
  "/assets/insta-6.jpg",
];

export default function Home() {
  const [inventoryCount, setInventoryCount] = useState(42);
  const [activeFilter, setActiveFilter] = useState("All");
  const [isScrolled, setIsScrolled] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const headerRef = useRef(null);

  // Handle scroll effects
  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 50);
      
      if (headerRef.current) {
        if (window.scrollY > 50) {
          headerRef.current.classList.add("scrolled");
        } else {
          headerRef.current.classList.remove("scrolled");
        }
      }
    };

    window.addEventListener("scroll", handleScroll, { passive: true });
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  // Scroll animations
  useEffect(() => {
    const observerOptions = {
      threshold: 0.1,
      rootMargin: "0px 0px -50px 0px",
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("in-view");
          observer.unobserve(entry.target);
        }
      });
    }, observerOptions);

    const animatedElements = document.querySelectorAll("[data-animate]");
    animatedElements.forEach((el) => observer.observe(el));

    return () => observer.disconnect();
  }, []);

  // Live inventory counter simulation
  useEffect(() => {
    const interval = setInterval(() => {
      setInventoryCount((prev) => {
        const change = Math.random() > 0.6 ? 1 : -1;
        return Math.min(52, Math.max(38, prev + change));
      });
    }, 5000);

    return () => clearInterval(interval);
  }, []);

  // Filter bikes
  const filteredBikes = activeFilter === "All" 
    ? bikes 
    : bikes.filter(bike => 
        activeFilter === "Under $5K" 
          ? parseInt(bike.price.replace(/[$,]/g, "")) < 5000
          : bike.category === activeFilter
      );

  return (
    <div id="top">
      {/* Header */}
      <header ref={headerRef} className="site-header">
        <div className="container header-inner">
          <a className="brand" href="#top">
            <div>
              <div className="brand-text">Get A Bike</div>
              <div className="brand-subtitle">Bakersfield</div>
            </div>
          </a>
          
          <nav className="nav">
            <a href="#inventory">Collection</a>
            <a href="#how-it-works">Experience</a>
            <a href="#testimonials">Reviews</a>
            <a href="#community">Community</a>
            <a href="#book" className="nav-cta">Book Private Viewing</a>
          </nav>
          
          <button 
            className="mobile-menu-btn"
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            aria-label="Toggle menu"
          >
            <span></span>
            <span></span>
            <span></span>
          </button>
        </div>
      </header>

      <main>
        {/* Hero Section */}
        <section className="hero" aria-labelledby="hero-title">
          <div className="hero-video-container">
            <img 
              src="/assets/hero-poster.jpg" 
              alt="" 
              className="hero-video"
            />
          </div>
          <div className="hero-overlay"></div>

          <div className="container hero-grid">
            <div className="hero-content">
              <div className="hero-eyebrow">Bakersfield, California</div>
              <h1 id="hero-title" className="hero-title">
                Certified Pre-Owned
                <span className="hero-title-accent">Performance Bicycles</span>
              </h1>
              <p className="hero-description">
                Bakersfield&apos;s exclusive destination for premium certified pre-owned bicycles. 
                Private appointment-only consultations. Expert fitting. 90-day comprehensive warranty. 
                Trade-in evaluations welcome.
              </p>
              <div className="hero-cta">
                <a className="btn btn-primary" href="#book">
                  Schedule Private Viewing
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                    <path d="M5 12h14M12 5l7 7-7 7"/>
                  </svg>
                </a>
                <a className="btn btn-secondary" href="#inventory">
                  View Collection
                </a>
              </div>
              <div className="hero-stats">
                <div className="stat-item">
                  <span className="stat-value">12+</span>
                  <span className="stat-label">Years Experience</span>
                </div>
                <div className="stat-item">
                  <span className="stat-value">2,500+</span>
                  <span className="stat-label">Bikes Sold</span>
                </div>
                <div className="stat-item">
                  <span className="stat-value">4.9</span>
                  <span className="stat-label">Google Rating</span>
                </div>
              </div>
            </div>

            <aside className="hero-widget" aria-label="Book appointment">
              <div className="widget-header">
                <h2 className="widget-title">Private Consultation</h2>
                <p className="widget-subtitle">Exclusive appointment-only service</p>
              </div>
              
              <form className="booking-form" onSubmit={(e) => e.preventDefault()}>
                <div className="form-group">
                  <label className="form-label">Service Type</label>
                  <select className="form-select">
                    <option>Private Bike Consultation (60 min)</option>
                    <option>Premium Test Ride (45 min)</option>
                    <option>Trade-In Valuation (30 min)</option>
                    <option>Professional Bike Fitting (90 min)</option>
                  </select>
                </div>
                
                <div className="form-group">
                  <label className="form-label">Preferred Date</label>
                  <input type="date" className="form-input" />
                </div>
                
                <div className="form-group">
                  <label className="form-label">Full Name</label>
                  <input type="text" placeholder="Your name" className="form-input" />
                </div>
                
                <div className="form-group">
                  <label className="form-label">Email Address</label>
                  <input type="email" placeholder="you@email.com" className="form-input" />
                </div>
                
                <button type="submit" className="btn btn-primary" style={{ width: "100%" }}>
                  Request Appointment
                </button>
              </form>
              
              <div className="widget-footer">
                <div className="live-indicator">
                  <span className="live-dot"></span>
                  <span>Live Inventory:</span>
                  <span className="inventory-count">{inventoryCount}</span>
                  <span>Premium Bikes</span>
                </div>
              </div>
            </aside>
          </div>
        </section>

        {/* Value Props Section */}
        <section className="value-props" aria-label="Why choose us">
          <div className="container">
            <div className="section-header" data-animate>
              <div className="section-eyebrow">The Experience</div>
              <h2 className="section-title">Why Discerning Riders Choose Us</h2>
              <p className="section-subtitle">
                Premium service, certified quality, and an appointment-only experience 
                that puts you first.
              </p>
            </div>
            
            <div className="props-grid">
              <article className="prop-card" data-animate>
                <div className="prop-icon">
                  <svg viewBox="0 0 24 24">
                    <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
                  </svg>
                </div>
                <h3 className="prop-title">Certified Pre-Owned</h3>
                <p className="prop-description">
                  Every bicycle undergoes a 72-point inspection by certified mechanics. 
                  Full service history, authenticated components, guaranteed authenticity.
                </p>
              </article>
              
              <article className="prop-card" data-animate>
                <div className="prop-icon">
                  <svg viewBox="0 0 24 24">
                    <path d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
                  </svg>
                </div>
                <h3 className="prop-title">Appointment-Only Service</h3>
                <p className="prop-description">
                  Your dedicated time with expert fitters. No crowds, no waiting, 
                  no pressure. Just focused attention on finding your perfect ride.
                </p>
              </article>
              
              <article className="prop-card" data-animate>
                <div className="prop-icon">
                  <svg viewBox="0 0 24 24">
                    <path d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/>
                  </svg>
                </div>
                <h3 className="prop-title">90-Day Warranty</h3>
                <p className="prop-description">
                  Ride with absolute confidence. Comprehensive mechanical warranty 
                  covering all components. Free adjustments included.
                </p>
              </article>
            </div>
          </div>
        </section>

        {/* Inventory Section */}
        <section className="inventory" id="inventory" aria-label="Featured inventory">
          <div className="container">
            <div className="inventory-header" data-animate>
              <div>
                <div className="section-eyebrow" style={{ justifyContent: "flex-start", marginBottom: "var(--space-4)" }}>
                  The Collection
                </div>
                <h2 className="section-title" style={{ textAlign: "left" }}>Curated Inventory</h2>
              </div>
              
              <div className="filter-tabs">
                {["All", "Road", "Gravel", "Mountain", "Electric", "Under $5K"].map((filter) => (
                  <button
                    key={filter}
                    className={`filter-tab ${activeFilter === filter ? "active" : ""}`}
                    onClick={() => setActiveFilter(filter)}
                  >
                    {filter}
                  </button>
                ))}
              </div>
            </div>
            
            <div className="inventory-grid">
              {filteredBikes.map((bike, index) => (
                <article key={bike.id} className="bike-card" data-animate style={{ transitionDelay: `${index * 100}ms` }}>
                  <div className="bike-image">
                    <img src={bike.image} alt={bike.name} loading="lazy" />
                  </div>
                  <div className="bike-info">
                    <div className="bike-category">{bike.category}</div>
                    <h3 className="bike-name">{bike.name}</h3>
                    <p className="bike-specs">{bike.specs}</p>
                    <div className="bike-price-row">
                      <span className="bike-price">{bike.price}</span>
                      <a href="#book" className="btn bike-btn">View Details</a>
                    </div>
                  </div>
                </article>
              ))}
            </div>
          </div>
        </section>

        {/* How It Works Section */}
        <section className="timeline" id="how-it-works" aria-label="How it works">
          <div className="container">
            <div className="section-header" data-animate>
              <div className="section-eyebrow">The Process</div>
              <h2 className="section-title">Your Journey to the Perfect Ride</h2>
              <p className="section-subtitle">
                A seamless, white-glove experience from browsing to riding.
              </p>
            </div>
            
            <div className="timeline-grid">
              <div className="step" data-animate>
                <div className="step-number">01</div>
                <h3 className="step-title">Browse Online</h3>
                <p className="step-description">
                  Explore our curated collection of certified pre-owned premium bicycles.
                </p>
              </div>
              
              <div className="step" data-animate>
                <div className="step-number">02</div>
                <h3 className="step-title">Book Appointment</h3>
                <p className="step-description">
                  Schedule your private consultation at your convenience.
                </p>
              </div>
              
              <div className="step" data-animate>
                <div className="step-number">03</div>
                <h3 className="step-title">Test & Fit</h3>
                <p className="step-description">
                  Experience the bikes with expert guidance and professional fitting.
                </p>
              </div>
              
              <div className="step" data-animate>
                <div className="step-number">04</div>
                <h3 className="step-title">Ride Confidently</h3>
                <p className="step-description">
                  Take home your perfect bike with full warranty and support.
                </p>
              </div>
            </div>
          </div>
        </section>

        {/* Testimonials Section */}
        <section className="testimonials" id="testimonials" aria-label="Customer testimonials">
          <div className="container">
            <div className="section-header" data-animate>
              <div className="section-eyebrow">Testimonials</div>
              <h2 className="section-title">Trusted by Serious Riders</h2>
              <p className="section-subtitle">
                Real experiences from cyclists who demand excellence.
              </p>
            </div>
            
            <div className="testimonials-grid">
              {testimonials.map((testimonial, index) => (
                <article key={testimonial.id} className="testimonial-card" data-animate style={{ transitionDelay: `${index * 100}ms` }}>
                  <div className="testimonial-stars">
                    {[...Array(testimonial.rating)].map((_, i) => (
                      <svg key={i} viewBox="0 0 24 24">
                        <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
                      </svg>
                    ))}
                  </div>
                  <p className="testimonial-text">&ldquo;{testimonial.text}&rdquo;</p>
                  <div className="testimonial-author">
                    <img src={testimonial.avatar} alt={testimonial.author} className="author-avatar" />
                    <div>
                      <div className="author-name">{testimonial.author}</div>
                      <div className="author-title">{testimonial.title}</div>
                    </div>
                  </div>
                </article>
              ))}
            </div>
            
            <div className="reviews-summary" data-animate>
              <div className="review-platform">
                <span className="review-platform-name">Google Reviews</span>
                <span className="review-platform-rating">4.9</span>
                <div className="review-platform-stars">
                  {[...Array(5)].map((_, i) => (
                    <svg key={i} viewBox="0 0 24 24">
                      <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
                    </svg>
                  ))}
                </div>
                <span className="review-count">127 reviews</span>
              </div>
              
              <div className="review-platform">
                <span className="review-platform-name">Yelp</span>
                <span className="review-platform-rating">5.0</span>
                <div className="review-platform-stars">
                  {[...Array(5)].map((_, i) => (
                    <svg key={i} viewBox="0 0 24 24">
                      <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
                    </svg>
                  ))}
                </div>
                <span className="review-count">89 reviews</span>
              </div>
              
              <div className="review-platform">
                <span className="review-platform-name">Facebook</span>
                <span className="review-platform-rating">4.8</span>
                <div className="review-platform-stars">
                  {[...Array(5)].map((_, i) => (
                    <svg key={i} viewBox="0 0 24 24">
                      <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
                    </svg>
                  ))}
                </div>
                <span className="review-count">56 reviews</span>
              </div>
            </div>
          </div>
        </section>

        {/* Community Section */}
        <section className="community" id="community" aria-label="Community">
          <div className="container">
            <div className="section-header" data-animate>
              <div className="section-eyebrow">Join Us</div>
              <h2 className="section-title">The Get A Bike Community</h2>
              <p className="section-subtitle">
                Events, rides, and resources for passionate cyclists.
              </p>
            </div>
            
            <div className="community-grid">
              <div className="community-card" data-animate>
                <h3 className="community-card-title">Upcoming Events</h3>
                <div className="event-list">
                  {events.map((event, index) => (
                    <div key={index} className="event-item">
                      <div className="event-name">{event.name}</div>
                      <div className="event-date">{event.date}</div>
                    </div>
                  ))}
                </div>
                <button className="btn btn-secondary" style={{ marginTop: "var(--space-4)", width: "100%" }}>
                  View All Events
                </button>
              </div>
              
              <div className="community-card" data-animate>
                <h3 className="community-card-title">Expert Insights</h3>
                <div className="blog-list">
                  {blogPosts.map((post, index) => (
                    <div key={index} className="blog-item">
                      <div className="blog-category">{post.category}</div>
                      <div className="blog-title">{post.title}</div>
                    </div>
                  ))}
                </div>
                <button className="btn btn-secondary" style={{ marginTop: "var(--space-4)", width: "100%" }}>
                  Read All Articles
                </button>
              </div>
              
              <div className="community-card" data-animate>
                <h3 className="community-card-title">Follow Our Journey</h3>
                <div className="insta-grid">
                  {instagramImages.map((img, index) => (
                    <div key={index} className="insta-item">
                      <img src={img} alt={`Instagram post ${index + 1}`} loading="lazy" />
                    </div>
                  ))}
                </div>
                <a 
                  href="https://instagram.com/getabike" 
                  target="_blank" 
                  rel="noopener noreferrer"
                  className="btn btn-secondary" 
                  style={{ marginTop: "var(--space-4)", width: "100%" }}
                >
                  @getabike
                </a>
              </div>
            </div>
          </div>
        </section>

        {/* Final CTA Section */}
        <section className="final-cta" id="book" aria-label="Book appointment">
          <div className="container cta-grid">
            <div className="cta-content" data-animate>
              <div className="hero-eyebrow">Begin Your Journey</div>
              <h2>Ready to Find Your Perfect Bike?</h2>
              <p>
                Schedule your private consultation today. Our expert team will guide you 
                through our curated collection and help you find the perfect ride for your style, 
                goals, and budget. Trade-in evaluations and professional fittings available.
              </p>
              
              <div className="cta-contacts">
                <div className="contact-item">
                  <div className="contact-icon">
                    <svg viewBox="0 0 24 24">
                      <path d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
                    </svg>
                  </div>
                  <div className="contact-info">
                    <span className="contact-label">Call Us</span>
                    <span className="contact-value">(661) 555-0100</span>
                  </div>
                </div>
                
                <div className="contact-item">
                  <div className="contact-icon">
                    <svg viewBox="0 0 24 24">
                      <path d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
                      <path d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
                    </svg>
                  </div>
                  <div className="contact-info">
                    <span className="contact-label">Visit By Appointment</span>
                    <span className="contact-value">213 E 18th St, Bakersfield</span>
                  </div>
                </div>
                
                <div className="contact-item">
                  <div className="contact-icon">
                    <svg viewBox="0 0 24 24">
                      <path d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
                    </svg>
                  </div>
                  <div className="contact-info">
                    <span className="contact-label">Email Us</span>
                    <span className="contact-value">concierge@getabike.com</span>
                  </div>
                </div>
              </div>
            </div>
            
            <div className="cta-widget" data-animate>
              <div className="widget-header">
                <h2 className="widget-title">Quick Booking</h2>
                <p className="widget-subtitle">We&apos;ll confirm within 2 hours</p>
              </div>
              
              <form className="booking-form" onSubmit={(e) => e.preventDefault()}>
                <div className="form-group">
                  <label className="form-label">Bike Interest</label>
                  <select className="form-select">
                    <option>Road / Racing</option>
                    <option>Gravel / Adventure</option>
                    <option>Mountain / Trail</option>
                    <option>Electric / E-Bike</option>
                    <option>Triathlon / TT</option>
                  </select>
                </div>
                
                <div className="form-group">
                  <label className="form-label">Budget Range</label>
                  <select className="form-select">
                    <option>Under $3,000</option>
                    <option>$3,000 - $5,000</option>
                    <option>$5,000 - $8,000</option>
                    <option>$8,000+</option>
                  </select>
                </div>
                
                <div className="form-group">
                  <label className="form-label">Phone Number</label>
                  <input type="tel" placeholder="(661) 555-0100" className="form-input" />
                </div>
                
                <div className="form-group">
                  <label className="form-label">Preferred Time</label>
                  <select className="form-select">
                    <option>Morning (9 AM - 12 PM)</option>
                    <option>Afternoon (12 PM - 5 PM)</option>
                    <option>Evening (5 PM - 7 PM)</option>
                    <option>Weekend</option>
                  </select>
                </div>
                
                <button type="submit" className="btn btn-primary" style={{ width: "100%" }}>
                  Schedule Consultation
                </button>
              </form>
            </div>
          </div>
        </section>
      </main>

      {/* Footer */}
      <footer className="site-footer">
        <div className="container">
          <div className="footer-grid">
            <div className="footer-brand">
              <div className="footer-brand-name">Get A Bike</div>
              <p className="footer-brand-tagline">
                Bakersfield&apos;s premier destination for certified pre-owned premium bicycles. 
                Expert fitting, 90-day warranty, appointment-only service.
              </p>
              <div className="footer-social">
                <a href="#" className="social-link" aria-label="Instagram">
                  <svg viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
                </a>
                <a href="#" className="social-link" aria-label="Facebook">
                  <svg viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
                </a>
                <a href="#" className="social-link" aria-label="YouTube">
                  <svg viewBox="0 0 24 24"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
                </a>
              </div>
            </div>
            
            <div className="footer-column">
              <h4>Services</h4>
              <div className="footer-links">
                <a href="#book">Private Consultations</a>
                <a href="#book">Professional Fitting</a>
                <a href="#book">Trade-In Evaluation</a>
                <a href="#">Bike Service</a>
                <a href="#">Warranty Support</a>
              </div>
            </div>
            
            <div className="footer-column">
              <h4>Inventory</h4>
              <div className="footer-links">
                <a href="#inventory">Road Bikes</a>
                <a href="#inventory">Gravel Bikes</a>
                <a href="#inventory">Mountain Bikes</a>
                <a href="#inventory">Electric Bikes</a>
                <a href="#inventory">New Arrivals</a>
              </div>
            </div>
            
            <div className="footer-column">
              <h4>Contact</h4>
              <div className="footer-links">
                <a href="tel:+16615550100">(661) 555-0100</a>
                <a href="mailto:concierge@getabike.com">concierge@getabike.com</a>
                <span>213 E 18th St</span>
                <span>Bakersfield, CA 93305</span>
                <span>Mon-Sat: 10 AM - 6 PM</span>
              </div>
            </div>
          </div>
          
          <div className="footer-bottom">
            <p className="footer-copyright">
              © {new Date().getFullYear()} Get A Bike Bicycles. All rights reserved.
            </p>
            <p className="footer-credits">
              Appointment Only • Premium Certified Bicycles • Bakersfield, CA
            </p>
          </div>
        </div>
      </footer>

      {/* Structured Data - LocalBusiness */}
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{
          __html: JSON.stringify({
            "@context": "https://schema.org",
            "@type": "BicycleStore",
            "@id": "https://getabike.com",
            "name": "Get A Bike Bicycles",
            "alternateName": "Get A Bike Bakersfield",
            "url": "https://getabike.com",
            "logo": "https://getabike.com/logo.jpg",
            "image": [
              "https://getabike.com/og-image.jpg",
              "https://getabike.com/assets/hero-poster.jpg"
            ],
            "description": "Bakersfield's premier certified pre-owned bicycle dealership. Premium road, gravel, mountain and electric bikes with appointment-only concierge service and 90-day warranty.",
            "slogan": "Certified Pre-Owned Performance Bicycles",
            "priceRange": "$$$",
            "currenciesAccepted": "USD",
            "paymentAccepted": "Cash, Credit Card, Debit Card, Financing",
            "telephone": "+1-661-555-0100",
            "email": "concierge@getabike.com",
            "address": {
              "@type": "PostalAddress",
              "streetAddress": "213 E 18th St",
              "addressLocality": "Bakersfield",
              "addressRegion": "CA",
              "postalCode": "93305",
              "addressCountry": "US"
            },
            "geo": {
              "@type": "GeoCoordinates",
              "latitude": "35.3733",
              "longitude": "-119.0187"
            },
            "openingHoursSpecification": [
              {
                "@type": "OpeningHoursSpecification",
                "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                "opens": "10:00",
                "closes": "18:00"
              },
              {
                "@type": "OpeningHoursSpecification",
                "dayOfWeek": "Saturday",
                "opens": "10:00",
                "closes": "18:00"
              }
            ],
            "areaServed": {
              "@type": "City",
              "name": "Bakersfield",
              "containedInPlace": {
                "@type": "State",
                "name": "California"
              }
            },
            "hasOfferCatalog": {
              "@type": "OfferCatalog",
              "name": "Bicycle Services",
              "itemListElement": [
                {
                  "@type": "Offer",
                  "itemOffered": {
                    "@type": "Service",
                    "name": "Private Bike Consultation"
                  }
                },
                {
                  "@type": "Offer",
                  "itemOffered": {
                    "@type": "Service",
                    "name": "Professional Bike Fitting"
                  }
                },
                {
                  "@type": "Offer",
                  "itemOffered": {
                    "@type": "Service",
                    "name": "Trade-In Evaluation"
                  }
                }
              ]
            },
            "aggregateRating": {
              "@type": "AggregateRating",
              "ratingValue": "4.9",
              "reviewCount": "127",
              "bestRating": "5",
              "worstRating": "1"
            },
            "review": testimonials.map(t => ({
              "@type": "Review",
              "author": {
                "@type": "Person",
                "name": t.author
              },
              "reviewRating": {
                "@type": "Rating",
                "ratingValue": t.rating.toString()
              },
              "reviewBody": t.text
            })),
            "sameAs": [
              "https://www.instagram.com/getabike",
              "https://www.facebook.com/getabikebakersfield",
              "https://www.yelp.com/biz/get-a-bike-bakersfield"
            ]
          }),
        }}
      />

      {/* Product Structured Data */}
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{
          __html: JSON.stringify({
            "@context": "https://schema.org",
            "@type": "ItemList",
            "itemListElement": bikes.map((bike, index) => ({
              "@type": "Product",
              "position": index + 1,
              "name": bike.name,
              "description": `${bike.category} bicycle - ${bike.specs}`,
              "category": bike.category,
              "brand": {
                "@type": "Brand",
                "name": bike.name.split(" ")[0]
              },
              "offers": {
                "@type": "Offer",
                "price": bike.price.replace(/[$,]/g, ""),
                "priceCurrency": "USD",
                "availability": "https://schema.org/InStock",
                "seller": {
                  "@type": "BicycleStore",
                  "name": "Get A Bike Bicycles"
                }
              }
            }))
          }),
        }}
      />

      {/* FAQ Structured Data */}
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{
          __html: JSON.stringify({
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
              {
                "@type": "Question",
                "name": "What makes Get A Bike different from other bike shops?",
                "acceptedAnswer": {
                  "@type": "Answer",
                  "text": "We specialize exclusively in certified pre-owned premium bicycles. Every bike undergoes a 72-point inspection by certified mechanics. We offer appointment-only service for personalized attention, professional fitting, and a 90-day comprehensive warranty on all bikes."
                }
              },
              {
                "@type": "Question",
                "name": "Do I need an appointment to visit?",
                "acceptedAnswer": {
                  "@type": "Answer",
                  "text": "Yes, we operate by appointment only to ensure every client receives our full attention. This allows us to provide a relaxed, no-pressure environment where you can take your time finding the perfect bike. Book online or call us at (661) 555-0100."
                }
              },
              {
                "@type": "Question",
                "name": "What is your warranty policy?",
                "acceptedAnswer": {
                  "@type": "Answer",
                  "text": "Every certified pre-owned bicycle comes with our comprehensive 90-day mechanical warranty. This covers all components and includes free adjustments. Extended warranty options are available for purchase."
                }
              },
              {
                "@type": "Question",
                "name": "Do you accept trade-ins?",
                "acceptedAnswer": {
                  "@type": "Answer",
                  "text": "Yes! We welcome trade-ins of quality bicycles. Our experts will evaluate your bike and provide a fair market value that can be applied toward your purchase. Schedule a trade-in evaluation appointment online or by phone."
                }
              },
              {
                "@type": "Question",
                "name": "Where are you located?",
                "acceptedAnswer": {
                  "@type": "Answer",
                  "text": "We are located at 213 E 18th St, Bakersfield, CA 93305. We serve cyclists throughout Kern County including Bakersfield, Delano, Oildale, and surrounding areas."
                }
              }
            ]
          }),
        }}
      />

      {/* Breadcrumb Structured Data */}
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{
          __html: JSON.stringify({
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
              {
                "@type": "ListItem",
                "position": 1,
                "name": "Home",
                "item": "https://getabike.com"
              }
            ]
          }),
        }}
      />
    </div>
  );
}
