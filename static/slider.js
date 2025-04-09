
document.addEventListener('DOMContentLoaded', function() {

    const rangeInput = document.getElementById('slider');
    const angmaks = document.getElementById('maks');

    function updateRangeTrack() {
        const value = rangeInput.value;
        const max = rangeInput.max;
        const percentage = (value / max) * 100;

        angmaks.style.display = 'inline-block';
        angmaks.style.width = '2em';
        angmaks.innerHTML = value;

    // Update the background gradient dynamically
        rangeInput.style.background = `linear-gradient(to right, hsl(171, 100%, 41%) 0%,
                                       hsl(171, 100%, 41%) ${percentage}%,
                                       #fff ${percentage}%, #fff 100%)`;
    };

    // Attach event listeners
    rangeInput.addEventListener('input', updateRangeTrack);
    // Initialize the track on page load
    updateRangeTrack();
});