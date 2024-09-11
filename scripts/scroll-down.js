const scrollToBottom = () => {
    const startTime = performance.now();
    const duration = 500; // Increased duration for smoother scrolling
    const startScrollTop = window.pageYOffset || document.documentElement.scrollTop;
    const endScrollTop = document.documentElement.scrollHeight - document.documentElement.clientHeight;
  
    const scrollStep = (currentTime) => {
      const progress = Math.min((currentTime - startTime) / duration, 1);
      window.scrollTo(0, startScrollTop + (endScrollTop - startScrollTop) * progress);
  
      if (progress < 1) {
        requestAnimationFrame(scrollStep);
      } else {
        // Double-check if we've reached the bottom, if not, force it
        if (window.innerHeight + window.pageYOffset < document.documentElement.scrollHeight) {
          window.scrollTo(0, document.documentElement.scrollHeight);
        }
      }
    };
  
    requestAnimationFrame(scrollStep);
  };
  
  // Call scrollToBottom when the page loads
  window.addEventListener('load', () => {
    setTimeout(scrollToBottom, 100); // Small delay to ensure content is fully loaded
  });
  
  // Remove the existing setTimeout calls at the end of the script
  // and replace them with this:
  window.addEventListener('load', () => {
    setTimeout(() => {
      scrollToBottom();
      document.getElementById('user-input').scrollIntoView({ behavior: 'smooth' });
    }, 100);
  });
  
  
  
  window.addEventListener('scroll', checkScrollPosition);
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-MKRXXLJQ6D"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-MKRXXLJQ6D');
</script>
