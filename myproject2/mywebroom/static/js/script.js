document.getElementById('bookingForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const startDate = document.getElementById('startDate').value;
    const startTime = document.getElementById('startTime').value;
    const endDate = document.getElementById('endDate').value;
    const endTime = document.getElementById('endTime').value;
    
    const confirmation = document.getElementById('confirmation');
    // confirmation.innerHTML = `Room booked from ${startDate} at ${startTime} to ${endDate} at ${endTime}.`;
    confirmation.innerHTML = `เลือกจองวันที่ ${startDate} เวลา ${startTime} จนถึงวันที่ ${endDate} เวลา ${endTime}.`;
    confirmation.style.display = 'block';
  });

function searchRoom() {
  var input, filter, items, item, h1, i, txtValue;
  input = document.getElementById('searchInput');
  filter = input.value.toUpperCase();
  items = document.getElementsByClassName('item-1');
  
  for (i = 0; i < items.length; i++) {
      item = items[i];
      h1 = item.getElementsByTagName('h1')[0];
      txtValue = h1.textContent || h1.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
          item.style.display = '';
      } else {
          item.style.display = 'none';
      }
  }
}
// // เรียกใช้งาน DOM
// document.addEventListener('DOMContentLoaded', function () {
//     // หาฟอร์ม
//     var form = document.querySelector('form');
    
//     // หาคำสั่งเมื่อฟอร์มถูกส่ง
//     form.addEventListener('บันทึก', function (event) {
//         event.preventDefault(); // ป้องกันการโหลดหน้าใหม่เมื่อฟอร์มถูกส่ง

//         // ดึงข้อมูลจากฟอร์ม
//         var firstName = form.querySelector('#fname').value;
//         var lastName = form.querySelector('#lname').value;
//         var email = form.querySelector('#email').value;
//         var subject = form.querySelector('#subject').value;

//         // สร้าง HTML element สำหรับแสดงข้อมูลผู้จอง
//         var reservationInfo = document.createElement('div');
//         reservationInfo.innerHTML = '<p>Name: ' + firstName + ' ' + lastName + '</p>' +
//             '<p>Email: ' + email + '</p>' +
//             '<p>Room Usage Details: ' + subject + '</p>';

//         // เพิ่มข้อมูลผู้จองไปยังหน้ารายการจอง
//         var bookingList = document.querySelector('.booking-list');
//         bookingList.appendChild(reservationInfo);

//         // ล้างข้อมูลในฟอร์มหลังจากที่ส่งข้อมูลไปแล้ว
//         form.reset();
//     });
// });