$(document).ready(function () {
    // example: https://getbootstrap.com/docs/4.2/components/modal/
    // show modal
    $('#task-modal').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget) // Button that triggered the modal
        const Instructor = button.data('source') // Extract info from data-* attributes
        const content = button.data('content') // Extract info from data-* attributes

        const modal = $(this)
        modal.find('.modal-title').text('Edit Course ' + Instructor)
        $('#course-form-display').attr('Instructor', Instructor)
    })

    $('#search-instructor').click(function () {
        $.ajax({
            type: 'POST',
            url: '/search_instructor',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'Instructor': $('#search-instructor-modal').find('.form-control-0').val()
            }),
            success: function (res) {
                console.log(res.response)
                location.href = "search_instructor"
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('#search-course').click(function () {
        $.ajax({
            type: 'POST',
            url: '/search_course',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'Subject': $('#search-course-modal').find('.form-control-0').val(),
                'Number': $('#search-course-modal').find('.form-control-1').val()
            }),
            success: function (res) {
                console.log(res.response)
                location.href = "search_course"
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('#search-ge').click(function () {
        $.ajax({
            type: 'POST',
            url: '/search_ge',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'ge_type': $('#search-ge-modal').find('.form-control-0').val()
            }),
            success: function (res) {
                console.log(res.response)
                location.href = "search_ge"
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('#search').click(function () {
        $.ajax({
            type: 'POST',
            url: '/search',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'Instructor': $('#search-modal').find('.form-control-0').val()
            }),
            success: function (res) {
                console.log(res.response)
                location.href = "search"  
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('#submit-insert').click(function () {
        console.log($('#insert-modal').find('.form-control-0').val());
        $.ajax({
            type: 'POST',
            url: '/insert',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'Instructor': $('#insert-modal').find('.form-control-0').val(),
                'Rating': $('#insert-modal').find('.form-control-1').val(),
                'Password': $('#insert-modal').find('.form-control-2').val(),
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('#submit-edit').click(function () {
        const tID = $('#course-form-display').attr('Instructor');
        console.log("******************")
        $.ajax({
            type: 'POST',
            url: '/edit/' + tID,
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'Instructor':$('#edit-modal').find('.form-control-2').val(),
                'Rating': $('#edit-modal').find('.form-control-0').val(),
                'Password': $('#edit-modal').find('.form-control-1').val(),
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('.remove').click(function () {
        const remove = $(this)
        $.ajax({
            type: 'POST',
            url: '/delete/' + remove.data('source'),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

});