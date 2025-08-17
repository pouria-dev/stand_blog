document.querySelectorAll('.reply-btn').forEach(function(btn){
    btn.addEventListener('click', function(){
        
        const username = this.dataset.username;
        const formId = this.dataset.formId;
        const formDiv = document.getElementById(formId);
        const textarea = formDiv.querySelector('.reply-textarea');


        formDiv.style.display = 'block';

        textarea.value = '@' + username + ' ';
        textarea.focus();
    });
});