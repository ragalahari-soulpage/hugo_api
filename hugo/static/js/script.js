// check, checkout submissions
var cameraStream;
var canvas;
var context;
function start_camera() {
  const video = document.querySelector("video");
  canvas = document.getElementById("canvas");
  context = canvas.getContext("2d");

  navigator.mediaDevices
    .getUserMedia({ video: true })
    .then(function (stream) {
      video.srcObject = stream;
      cameraStream = stream;
    })
    .catch(function (error) {
      console.log(
        "The following error occurred when trying to use getUserMedia: " + err
      );
    });
}

$(window).on("shown.bs.modal", function () {
  $("#myModal").modal("show");
  start_camera();
});
$(window).on("hidden.bs.modal", function () {
  $("#myModal").modal("hide");
  cameraStream.getTracks().forEach(function (track) {
    track.stop();
  });
});

function spinners_loading() {
  return $("#status-message").replaceWith(`
  <div id="status-message" class="p-3">
  <div class="spinner-grow text-primary"></div>
  <div class="spinner-grow text-success"></div>
  <div class="spinner-grow text-info"></div>
  <div class="spinner-grow text-warning"></div>
  </div>
  `);
}

// Ajax calls for form submission

$("#checkin").click(function (e) {
  e.preventDefault();

  context.drawImage(video, 0, 0, 640, 480);
  var data = {
    checkin_image: canvas.toDataURL(),
    checkin_notes: document.getElementById("checkin_notes").value,
    csrfmiddlewaretoken: $.cookie("csrftoken"),
  };
  $("#check-msg").hide();
  spinners_loading();
  $.ajax({
    url: "/api/check-in/",
    type: "POST",
    data: data,
    success: function (result) {
      update_status();
      $(".close").remove();
      $("#snap-modal-close").click(function (e) {
        location.reload();
      });
    },
    // error: function (xhr, textStatus, error) {
    //   $("#check-msg").show();
    //   $("#status-message").empty();
    //   $("#status-message").append(`${xhr.responseText}`);
    // },
  });
});

$("#checkin-breakin").click(function (e) {
  e.preventDefault();
  $("#check-msg").hide();
  spinners_loading();
  $.ajax({
    url: "/api/check-in/",
    type: "PUT",
    beforeSend: function (xhr) {
      xhr.setRequestHeader("X-CSRFToken", $.cookie("csrftoken"));
    },
    success: function (result) {
      update_status();
      $(".close").remove();
      $("#snap-modal-close").click(function (e) {
        location.reload();
      });
    },
    // error: function (xhr, textStatus, error) {
    //   $("#check-msg").show();
    //   $("#status-message").empty();
    //   $("#status-message").append(`${xhr.responseText}`);
    // },
  });
});

$("#checkout").click(function (e) {
  e.preventDefault();

  context.drawImage(video, 0, 0, 640, 480);
  var data = {
    checkout_image: canvas.toDataURL(),
    checkout_notes: document.getElementById("checkout_notes").value,
  };
  $("#check-msg").hide();
  spinners_loading();
  $.ajax({
    url: "/api/check-out/",
    type: "PUT",
    data: data,
    beforeSend: function (xhr) {
      xhr.setRequestHeader("X-CSRFToken", $.cookie("csrftoken"));
    },
    success: function (result) {
      update_status();
      $(".close").remove();
      $("#snap-modal-close").click(function (e) {
        location.reload();
      });
    },
    // error: function (xhr, textStatus, error) {
    //   $("#check-msg").show();
    //   $("#status-message").empty();
    //   $("#status-message").append(`${xhr.responseText}`);
    // },
  });
});

$(".employee-submit").click(function (e) {
  e.preventDefault();
  console.log("hitted");
  $form = document.getElementById("employee-form");
  var formData = new FormData($form);
  formData.append("csrfmiddlewaretoken", $.cookie("csrftoken"));
  $.ajax({
    url: "/api/employee/",
    type: "POST",
    data: formData,
    success: function (response) {
      // location.reload();
    },
    cache: false,
    contentType: false,
    processData: false,
  });
});

$(".employee-update").click(function (e) {
  e.preventDefault();
  console.log("hitted");
  $form = document.getElementById("employee-form");
  var formData = new FormData($form);

  $.ajax({
    url: "/api/employee/",
    type: "PUT",
    data: formData,
    beforeSend: function (xhr) {
      xhr.setRequestHeader("X-CSRFToken", $.cookie("csrftoken"));
    },
    success: function (response) {
      // location.reload();
    },
    cache: false,
    contentType: false,
    processData: false,
  });
});

// checkin, checkout submissions ends

// uploaded image preview
function showImage(src, target) {
  var fr = new FileReader();
  fr.onload = function () {
    target.src = fr.result;
  };
  fr.readAsDataURL(src.files[0]);
}
function putImage() {
  var src = document.getElementById("select_image");
  var target = document.getElementById("target");
  showImage(src, target);
}

// handle selected options
$("#input-month").change(function (e) {
  var year = $("#input-year").val();
  if (year !== null) {
    location.href = `?month=${this.value}&year=${year}`;
  } else {
    location.href = `?month=${this.value}`;
  }
});

// handle selected options
$("#input-user").change(function (e) {
  location.href = `?employee=${this.value}`;
});

// add active class to current paged side menu
$(function () {
  $('a[href="' + location.pathname + '"]')
    .find(".menu-icons")
    .toggleClass("menu-inactive");
  $('a[href="' + location.pathname + '"]')
    .children(".menu-item")
    .toggleClass("active");
});

// add class for attendance table for responsive
function checkWidth(init) {
  if ($(window).width() < 1200) {
    $(".month").addClass("table-responsive");
    $(".attendance-table").addClass("table-responsive");
  } else {
    if (!init) {
      $(".month").removeClass("table-responsive");
      $(".attendance-table").removeClass("table-responsive");
    }
  }
}

$(document).ready(function () {
  $(".profile-header").click(function () {
    $(this).addClass("active");
    $(".profile-header").not(this).removeClass("active");
  });
});

$(document).ready(function () {
  checkWidth(true);

  $(window).resize(function () {
    checkWidth(false);
  });
});

// search for employee
function searchEmployee() {
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("search-employee");
  filter = input.value.toUpperCase();
  table = document.getElementById("employees-table");
  tr = table.getElementsByTagName("tr");
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[0];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}

// adds default height for sidebar to full page
if ($(".sidebar").height() < 950) {
  $(".sidebar").height(950);
}

$("#export-sheet").attr("href", "/api/export/" + window.location.search);

$(document).ready(function () {
  $("#add_emp").click(function (e) {
    e.preventDefault();
    add_employment();
  });
});

$(".employments").on("click", ".remove_emp", function (e) {
  e.preventDefault();

  $(this).parent().remove();
});

$(document).ready(function () {
  $("#add_edu").click(function (e) {
    e.preventDefault();
    add_education();
  });
});

$(".educations").on("click", ".remove_edu", function (e) {
  e.preventDefault();

  $(this).parent().remove();
});
