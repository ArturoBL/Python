from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base
from models.Obras import Obra

# -----------------------------------------
# Modelo Presupuesto
# -----------------------------------------

class Presupuesto(Base):
    __tablename__ = "presupuestos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    descripcion: Mapped[str] = mapped_column(String(200))

    # Foreign key física
    obra_id: Mapped[int] = mapped_column(
        ForeignKey("obras.id")
    )

    # Relación hacia Obra
    obra: Mapped["Obra"] = relationship(
        back_populates="presupuestos"
    )