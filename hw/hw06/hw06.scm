;;;;;;;;;;;;;;;
;; Questions ;;
;;;;;;;;;;;;;;;

; Scheme

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  'YOUR-CODE-HERE
  (car (cdr s))
)

(define (caddr s)
  'YOUR-CODE-HERE
  (car (cdr (cdr s)))
)

(define (sign x)
  'YOUR-CODE-HERE
  (cond
  	((< x 0) -1)
  	((= x 0) 0)
  	(else 1))
)

(define (square x) (* x x))

(define (pow b n)
  'YOUR-CODE-HERE
  (cond
  	((= n 1) b)
  	((= n 2) (square b))
  	((even? n) (* (square b) (pow b (- n 2))))
  	((odd? n) (* b (pow b (- n 1)))))
)

(define (unique s)
  'YOUR-CODE-HERE
  (if (null? s) s
  	(cons (car s) 
  		(unique (filter (lambda (x) (not (equal? (car s) x))) (cdr s)))))
)

'guer  
(define (sixty-ones lst)
	(cond 
		((null? lst) 0)
		((= 6 (car lst)) (if (= 1 (car (cdr lst))) 
						 	(+ 1 (sixty-ones (cdr (cdr lst))))
						 	(sixty-ones (cdr lst))))
		(else (sixty-ones (cdr lst)))
	)
)

(define (no-elevens n)
	(cond
		((zero? n) nil)
		(else (cons (cons 6 (no-elevens (- n 1)) (no-elevens (- n 1)))))
	)
)

 	