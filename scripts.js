document.addEventListener("DOMContentLoaded", function() {
    fetch('posts.json')
        .then(response => response.json())
        .then(posts => {
            const postsList = document.getElementById('posts');
            posts.forEach(post => {
                const listItem = document.createElement('li');
                const link = document.createElement('a');
                link.href = post.url;
                link.textContent = post.title;
                listItem.appendChild(link);
                postsList.appendChild(listItem);
            });
        });
});
