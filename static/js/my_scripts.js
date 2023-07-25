/*!
* Start Bootstrap - Clean Blog v6.0.9 (https://startbootstrap.com/theme/clean-blog)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-clean-blog/blob/master/LICENSE)
*/
window.addEventListener('DOMContentLoaded', () => {
    let scrollPos = 0;
    const mainNav = document.getElementById('mainNav');
    const headerHeight = mainNav.clientHeight;
    window.addEventListener('scroll', function() {
        const currentTop = document.body.getBoundingClientRect().top * -1;
        if ( currentTop < scrollPos) {
            // Scrolling Up
            if (currentTop > 0 && mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-visible');
            } else {
                console.log(123);
                mainNav.classList.remove('is-visible', 'is-fixed');
            }
        } else {
            // Scrolling Down
            mainNav.classList.remove(['is-visible']);
            if (currentTop > headerHeight && !mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-fixed');
            }
        }
        scrollPos = currentTop;
    });
})

document.addEventListener("DOMContentLoaded", function () {
    var dropdowns = document.querySelectorAll(".dropdown-toggle");
    var dropdownMenus = document.querySelectorAll(".dropdown-menu");

    // 드롭다운 토글 버튼에 호버 이벤트 리스너를 추가합니다.
    dropdowns.forEach(function (dropdown) {
      dropdown.addEventListener("mouseover", function () {
        var dropdownMenu = this.nextElementSibling;
        dropdownMenu.classList.add("show");
      });

      dropdown.addEventListener("mouseout", function () {
        var dropdownMenu = this.nextElementSibling;
        dropdownMenu.classList.remove("show");
      });
    });

    // 드롭다운 메뉴에 호버 이벤트 리스너를 추가합니다.
    dropdownMenus.forEach(function (menu) {
      menu.addEventListener("mouseover", function () {
        this.classList.add("show");
      });

      menu.addEventListener("mouseout", function () {
        this.classList.remove("show");
      });
    });
  });