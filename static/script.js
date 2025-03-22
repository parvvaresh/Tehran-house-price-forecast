document.addEventListener('DOMContentLoaded', function() {
    // Search functionality
    const searchInput = document.getElementById('addressSearch');
    const addressSelect = document.getElementById('address');
    
    if(searchInput && addressSelect) {
        searchInput.addEventListener('input', function(e) {
            const searchTerm = e.target.value.toLowerCase();
            const options = addressSelect.options;
            
            for (let i = 0; i < options.length; i++) {
                const optionText = options[i].text.toLowerCase();
                options[i].style.display = optionText.includes(searchTerm) ? '' : 'none';
            }
        });
    }

    // Range updates
    function updateRangeDisplay(rangeId, displayId, suffix = '') {
        const range = document.getElementById(rangeId);
        const display = document.getElementById(displayId);
        
        if(range && display) {
            range.addEventListener('input', function(e) {
                display.textContent = e.target.value + suffix;
            });
        }
    }

    updateRangeDisplay('area', 'areaValue', ' متر');
    updateRangeDisplay('year', 'yearValue');
    updateRangeDisplay('rooms', 'roomsValue', ' اتاق');
});