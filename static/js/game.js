var now_char = 'X';

function query_move(move, target) {
    target.innerHTML = now_char;
    now_char = now_char == 'X' ? 'O' : 'X';
    $.ajax({
        url: '/move',
        type: 'POST',
        contentType: "application/json",
        data: JSON.stringify({
            move: move,
            csrfmiddlewaretoken: '{{ csrf_token }}'
        }),
        success: function (data) {
            console.log("success");
            console.log(data);
            if(data['gameover']){
                if(data['draw']){
                    Swal.fire({
                        icon: 'info',
                        title: 'Game over!',
                        text: 'It\'s a draw!',
                    }).then((result) => {
                        if (result.isConfirmed) {
                            window.location = '/stat'
                        }
                    })
                }else{
                    Swal.fire({
                        icon: 'info',
                        title: 'Game over!',
                        text: 'Player ' + data['winner'] + ' won!',
                    }).then((result) => {
                        if (result.isConfirmed) {
                            window.location = '/stat'
                        }
                    })
                }
            }
        },
        error: function (data) {
            console.log("error");
            console.log(data);
        }
    });
}

document.querySelectorAll(".square").forEach(item => {
    item.addEventListener('click', event => {
        //handle click 
        cell_id = event.target.id;
        console.log(cell_id);
        const re = new RegExp('square(\\d+)');
        const match = re.exec(cell_id);
        if(match == null){
            Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: 'This cell is already occupied! Try another one.',
            })
            return;
        }
        square_id = parseInt(match[1]);
        query_move(square_id, event.target);
    })
})

