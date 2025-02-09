let compassContainer = null;
let isCompassVisible = false;

// Handle messages from background
chrome.runtime.onMessage.addListener((message) => {
  if (message.action === "toggleCompass") {
    toggleCompass();
  }
});

function toggleCompass() {
  if (isCompassVisible) {
    hideCompass();
  } else {
    showCompass();
  }
  isCompassVisible = !isCompassVisible;
}

function showCompass() {
  if (!compassContainer) {
    createCompass();
  }
  compassContainer.style.display = "block";
}

function hideCompass() {
  if (compassContainer) {
    compassContainer.style.display = "none";
  }
}

function createCompass() {
  // Create the container
  compassContainer = document.createElement('div');
  compassContainer.id = 'compass-overlay-container';

  // Create the compass image element
  const compass = document.createElement('img');
  compass.src = chrome.runtime.getURL('compass_rose.png'); // Provide your own image file in the extension directory
  compass.id = 'compass-image';

  // Append image to container
  compassContainer.appendChild(compass);

  // Add container to body
  document.body.appendChild(compassContainer);

  // Enable dragging
  enableDragging(compassContainer);

  // Add UI for scaling: For simplicity, we’ll listen to mousewheel on the container for scaling
  compassContainer.addEventListener('wheel', (e) => {
    e.preventDefault();
    // scale up or down
    const currentScale = parseFloat(compassContainer.getAttribute('data-scale')) || 1;
    let newScale = currentScale + (e.deltaY < 0 ? 0.1 : -0.1);
    if (newScale < 0.1) newScale = 0.1; // limit minimum size
    compassContainer.style.transform = `scale(${newScale})`;
    compassContainer.setAttribute('data-scale', newScale);
  });
}

function enableDragging(element) {
  let isDragging = false;
  let startX, startY;

  element.addEventListener('mousedown', onMouseDown);

  function onMouseDown(e) {
    isDragging = true;
    startX = e.clientX - element.offsetLeft;
    startY = e.clientY - element.offsetTop;
    document.addEventListener('mousemove', onMouseMove);
    document.addEventListener('mouseup', onMouseUp);
  }

  function onMouseMove(e) {
    if (!isDragging) return;
    element.style.left = (e.clientX - startX) + 'px';
    element.style.top = (e.clientY - startY) + 'px';
  }

  function onMouseUp() {
    isDragging = false;
    document.removeEventListener('mousemove', onMouseMove);
    document.removeEventListener('mouseup', onMouseUp);
  }
}
