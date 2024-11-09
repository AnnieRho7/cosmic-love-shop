function showMessage(message, type = 'success') {
    const messageHtml = `
        <div class="alert alert-${type} alert-dismissible fade show" role="alert">
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>`;
    $('.alert-banner').html(messageHtml);
    
    setTimeout(function() {
        $('.alert-banner .alert').fadeOut('slow', function() {
            $(this).remove();
        });
    }, 3000);
}

function updateWishlistButtons(productId, isInWishlist) {
    $(`.wishlist-btn[data-product-id="${productId}"]`).each(function() {
        const $btn = $(this);
        const $icon = $btn.find('i');
        const $text = $btn.find('.wishlist-text');

        if (isInWishlist) {
            $btn.addClass('active');
            $icon.removeClass('far').addClass('fas');
            if ($text.length) {
                $text.text('Remove from Wishlist');
            }
        } else {
            $btn.removeClass('active');
            $icon.removeClass('fas').addClass('far');
            if ($text.length) {
                $text.text('Add to Wishlist');
            }
        }
    });
}

function initWishlistButtons() {
    $('.wishlist-btn').click(function(e) {
        e.preventDefault();
        const $btn = $(this);
        const productId = $btn.data('product-id');
        const url = $btn.data('add-to-wishlist-url');

        $.ajax({
            url: url,
            type: 'POST',
            headers: {
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            },
            success: function(data) {
                showMessage(data.message, data.status === 'added' ? 'success' : 'info');
                updateWishlistButtons(data.product_id, data.in_wishlist);
            },
            error: function(xhr, status, error) {
                showMessage('There was an error updating your wishlist.', 'danger');
            }
        });
    });
}

function checkInitialWishlistStatus() {
    $('.wishlist-btn').each(function() {
        const $btn = $(this);
        const productId = $btn.data('product-id');
        
        $.get(`/users/wishlist/status/${productId}/`, function(data) {
            if (data.in_wishlist) {
                updateWishlistButtons(productId, true);
            }
        });
    });
}

$(document).ready(function() {
    initWishlistButtons();
    checkInitialWishlistStatus();
});