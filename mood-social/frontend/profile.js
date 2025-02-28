document.addEventListener("DOMContentLoaded", function() {
    const moodSelector = document.getElementById('moodSelector');
    const body = document.body;
    const profilePic = document.querySelector('.profile-pic');
    const themeToggle = document.getElementById('themeToggle');

    const moodColors = {
        happy: { color: '#f7b500', dark: '#d69600' },
        chill: { color: '#00a8cc', dark: '#007a99' },
        excited: { color: '#ff477e', dark: '#d4305c' },
        creative: { color: '#8a2be2', dark: '#6a1bb5' }
    };

    setMoodColor(moodSelector.value);

    moodSelector.addEventListener('change', () => {
        setMoodColor(moodSelector.value);
    });

    themeToggle.addEventListener('click', () => {
        body.classList.toggle('light-mode');
        body.classList.toggle('dark-mode');
    });

    function setMoodColor(mood) {
        const { color, dark } = moodColors[mood] || moodColors['chill'];
        document.documentElement.style.setProperty('--mood-color', color);
        document.documentElement.style.setProperty('--mood-dark-color', dark);
        profilePic.style.borderColor = color;
    }
});
