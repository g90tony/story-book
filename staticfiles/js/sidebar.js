/* Set the width of the sidebar to 300px and the left margin of the page content to 300px */
function openNav() {
  document.getElementById("sidebar").style.visibility = "visible";
  document.getElementById("sidebar").style.display = "flex";
}

/* Set the width of the sidebar to 0 and the left margin of the page content to 0 */
function closeNav() {
  document.getElementById("sidebar").style.visibility = "hidden";
}

let sidebar_tracker = true;

function sidebar_toggle() {
  if (!sidebar_tracker) {
    openNav();
    sidebar_tracker = true;
  } else {
    closeNav();
    sidebar_tracker = false;
  }
}

function viewport_tracker() {
  if (document.body.clientWidth <= 576) {
    closeNav();
    sidebar_tracker = false;
  } else {
    openNav();
  }
}
